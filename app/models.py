from dataclasses import dataclass


@dataclass
class Product:
    entity_id: str
    name: str
    link: str
    description: str

    keys: list[str]
    job_levels: list[str]
    languages: list[str]

    duration: str
    adaptive: str
    remote: str