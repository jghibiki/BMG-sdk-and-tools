from typing import Dict
from compendium.models.character_affiliation import CharacterAffiliation


def load_character_affiliation(data: Dict, compendium: "Compendium"):
    return CharacterAffiliation(
        data["affiliation_id"],
        data["can_be_team_boss"],
        data["always_team_boss"],
        compendium
    )