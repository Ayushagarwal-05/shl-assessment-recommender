"""Extract the SHL product catalog JSON embedded in a pretty-printed PDF."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pdfplumber

# Paths relative to the project root.
PDF_PATH = Path(__file__).resolve().parent / "data" / "shl_product_catalog.pdf"
OUTPUT_PATH = Path(__file__).resolve().parent / "data" / "catalog.json"

# Repeated page headers in the PDF overlay "Pretty-print" onto JSON keys and values.
# These mappings restore the original text for each known garbled fragment.
GARBLED_KEY_MAP: dict[str, str] = {
    'ya-dparpitnitve"': "adaptive",
    'yd-epsrcirnitption"': "description",
    'yd-uprraitniton"': "duration",
    'yd-uprraitniton_raw"': "duration_raw",
    'ye-nptriitnyt_id"': "entity_id",
    'yj-opbr_ilnetvels"': "job_levels",
    'yj-opbr_ilnetvels_raw"': "job_levels_raw",
    'yk-epyrsi"n': "keys",
    'yl-apnrgiunatges"': "languages",
    'yl-apnrgiunatges_raw"': "languages_raw",
    'yl-ipnrki"n': "link",
    'yn-apmrei"n': "name",
    'yr-epmroitnet"': "remote",
    'ys-cprraipnetd_at"': "scraped_at",
    'ys-tpartiunst"': "status",
}

GARBLED_VALUE_MAP: dict[str, str] = {
    "Arbiinltity & Aptitude": "Ability & Aptitude",
    "Drainnitsh": "Danish",
    "Druitncth": "Dutch",
    "Ernignltish (USA)": "English (USA)",
    "Ernignltish International": "English International",
    "Ernitnrty-Level": "Entry-Level",
    "Erxienctutive": "Executive",
    "Frrienntch": "French",
    "Frrionntt Line Manager": "Front Line Manager",
    "Grriandtuate": "Graduate",
    "Irnidnotnesian": "Indonesian",
    "Irtianltian": "Italian",
    "Krnionwtledge & Skills": "Knowledge & Skills",
    "Mrainnatger": "Manager",
    "Mriidn-tProfessional": "Mid-Professional",
    "Prrionftessional Individual Contributor": "Professional Individual Contributor",
    "Sreirnbtian": "Serbian",
    "Sriimnutlations": "Simulations",
    "Sruipnetrvisor": "Supervisor",
}


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Read every page and concatenate extracted text."""
    page_texts: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_texts.append(page.extract_text() or "")
    return "\n".join(page_texts)


def repair_garbled_line(line: str) -> str | None:
    """Repair or drop a single line corrupted by PDF page headers."""
    stripped = line.strip()

    if stripped == "Pretty-print":
        return None

    if stripped == "P re{tty-print":
        return "{"

    if stripped == "P re}tty-print":
        return "}"

    if stripped == "P re}t,ty-print":
        return "},"

    if stripped == "P r e tt]y-print":
        return "]"

    if stripped == "P r e tt]y,-print":
        return "],"

    # Header merged with a JSON key, e.g. P r e tt"yl-ipnrki"n:t "https://..."
    if line.startswith('P r e tt"'):
        remainder = line[len('P r e tt"'):]
        for garbled, correct in sorted(
            GARBLED_KEY_MAP.items(), key=lambda item: len(item[0]), reverse=True
        ):
            garbled_prefix = garbled.split('"')[0]
            if not remainder.startswith(garbled_prefix):
                continue

            suffix = remainder[len(garbled_prefix):]
            # Remove overlay artifacts between the garbled key and the JSON value.
            suffix = re.sub(r'^"n:t\s*', "", suffix)
            suffix = re.sub(r'^":\s*', "", suffix)
            suffix = re.sub(r'^n:t\s*', "", suffix)
            suffix = re.sub(r'^:t\s*', "", suffix)
            return f'"{correct}": {suffix}'

    # Header merged with a JSON string value, e.g. P r e t t y-"pErnignltish (USA)"
    value_match = re.match(r'^P r e t t y-"p(.+?)"(,?)$', line)
    if value_match:
        garbled_value = value_match.group(1)
        trailing_comma = value_match.group(2)
        restored = GARBLED_VALUE_MAP.get(garbled_value, garbled_value)
        return f'"{restored}"{trailing_comma}'

    return line


def clean_extracted_text(raw_text: str) -> str:
    """Remove header artifacts and normalise PDF line breaks."""
    repaired_lines: list[str] = []
    for line in raw_text.splitlines():
        repaired = repair_garbled_line(line)
        if repaired is not None:
            repaired_lines.append(repaired)

    text = "\n".join(repaired_lines)

    # PDF wraps long strings across lines; join hyphenated word breaks first.
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)

    # Replace raw newlines inside JSON string literals with spaces.
    text = _collapse_newlines_inside_strings(text)

    return text


def _collapse_newlines_inside_strings(text: str) -> str:
    """Convert unescaped newlines inside JSON strings to spaces."""
    output: list[str] = []
    in_string = False
    escaped = False

    for char in text:
        if escaped:
            output.append(char)
            escaped = False
            continue

        if char == "\\" and in_string:
            output.append(char)
            escaped = True
            continue

        if char == '"':
            in_string = not in_string
            output.append(char)
            continue

        if in_string and char == "\n":
            output.append(" ")
            continue

        output.append(char)

    return "".join(output)


def reconstruct_json_array(text: str) -> str:
    """Ensure the extracted text is wrapped as a JSON array."""
    text = text.strip()

    if not text.startswith("["):
        text = "[\n" + text

    if not text.endswith("]"):
        text = text.rstrip(",\n") + "\n]"

    return text


def parse_catalog_json(text: str) -> list[dict]:
    """Parse the reconstructed JSON text into Python objects."""
    return json.loads(text)


def save_catalog(catalog: list[dict], output_path: Path) -> None:
    """Write the catalog to disk with stable formatting."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(catalog, file, indent=2, ensure_ascii=False)
        file.write("\n")


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Catalog PDF not found: {PDF_PATH}")

    raw_text = extract_text_from_pdf(PDF_PATH)
    cleaned_text = clean_extracted_text(raw_text)
    json_text = reconstruct_json_array(cleaned_text)
    catalog = parse_catalog_json(json_text)

    save_catalog(catalog, OUTPUT_PATH)

    total_products = len(catalog)
    first_name = catalog[0]["name"] if catalog else ""
    last_name = catalog[-1]["name"] if catalog else ""

    print(f"total products: {total_products}")
    print(f"first product name: {first_name}")
    print(f"last product name: {last_name}")


if __name__ == "__main__":
    main()
