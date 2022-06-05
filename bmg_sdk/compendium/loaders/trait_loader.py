from typing import Dict
from compendium.models.trait import Trait, TraitReference


def load_trait_reference(data: Dict, compendium: "Compendium"):
    return TraitReference(
        data["trait_id"],
        data["alternate_name"],
        compendium
    )


def load_trait(data: Dict, compendium: "Compendium"):
    return Trait(
        data["id"],
        data["name"],
        data["description"],
        compendium
    )