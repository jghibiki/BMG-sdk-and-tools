from typing import Dict
from compendium.models.affiliation import Affiliation
from compendium.models.compendium import Compendium


def load_affiliation(data: Dict, compendium: Compendium):
    return Affiliation(
        data["id"],
        data["name"],
        data["image"],
        data["icon"],
        data["is_team"],
        data["eternal"],
        compendium
    )
