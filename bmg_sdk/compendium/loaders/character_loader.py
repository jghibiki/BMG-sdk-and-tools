from typing import Dict

from bmg_sdk.compendium.loaders.character_affiliation_loader import load_character_affiliation
from bmg_sdk.compendium.loaders.trait_loader import load_trait_reference
from bmg_sdk.compendium.models.character import Character
from bmg_sdk.compendium.models.compendium import Compendium


def load_character(data: Dict, compendium: Compendium):
    return Character(
        id=data["id"],
        name=data["name"],
        alias=data["alias"],
        affiliations=[
            load_character_affiliation(a, compendium)
            for a in data["affiliations"]
        ],
        rival_affiliations_ids=data["rival_affiliation_ids"],
        rank_ids=data["rank_ids"],
        weapon_ids=data["weapon_ids"],
        image=data["image"],
        background=data["background"],
        willpower=data["willpower"],
        strength=data["strength"],
        movement=data["movement"],
        attack=data["attack"],
        defense=data["defense"],
        special=data["special"],
        endurance=data["endurance"],
        reputation=data["reputation"],
        funding=data["funding"],
        eternal=data["eternal"],
        bases_size=data["bases_size"],
        traits= [
            load_trait_reference(t, compendium)
            for t in data["traits"]
        ],
        upgrade_ids=data["upgrade_ids"],
        compendium=compendium
    )