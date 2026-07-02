import re


class IntentExtractor:
    def extract(self, messages):
        text = " ".join(
            m["content"] for m in messages if m["role"] == "user"
        ).lower()

        info = {
            "role": None,
            "purpose": None,
            "skills": [],
            "compare": False,
            "refine": False,
        }

        # Purpose
        if "selection" in text or "hire" in text or "recruit" in text:
            info["purpose"] = "selection"

        elif "development" in text or "upskill" in text:
            info["purpose"] = "development"

        # Compare
        comparison_words = [
            "compare",
            "comparison",
            "difference",
            "vs",
            "versus",
            "between"
        ]

        info["compare"] = any(
            word in text
            for word in comparison_words
        )

        # Refinement
        if any(word in text for word in [
            "instead",
            "also",
            "add",
            "remove",
            "replace"
        ]):
            info["refine"] = True

        # Skills
        skills = [
            "java",
            "python",
            "sql",
            "aws",
            "azure",
            "react",
            "javascript",
            "c++",
            "c#",
            "leadership",
            "sales",
            "finance"
        ]

        for skill in skills:
            if skill in text:
                info["skills"].append(skill)

        # Role
        roles = [
            "developer",
            "engineer",
            "manager",
            "director",
            "executive",
            "graduate",
            "intern"
        ]

        for role in roles:
            if role in text:
                info["role"] = role
                break

        return info