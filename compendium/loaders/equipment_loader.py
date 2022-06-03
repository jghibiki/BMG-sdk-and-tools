from typing import Dict
from unidecode import unidecode

from compendium.loaders.trait_loader import load_trait_reference
from compendium.models.compendium import Compendium
from compendium.models.equipment import Equipment
from compendium.models.trait import TraitReference


def load_equipment(data: Dict, compendium: Compendium):
    return Equipment(
        id=data["id"],
        name=data["name"],
        description=unidecode(data["description"]) if data["description"] else None,
        max_count=data["max_count"],
        funding=data["funding"],
        reputation=data["reputation"],
        image=data["image"],
        banned_character_ids=data["banned_character_ids"],
        banned_crew_equipment_ids=data["banned_crew_equipment_ids"],
        required_character_ids=data["required_character_ids"],
        required_crew_character_ids=data["required_crew_character_ids"],
        required_rank_ids=data["required_rank_ids"],
        required_affiliation_ids=data["required_affiliation_ids"],
        weapon_ids=data["weapon_ids"],
        traits=[
            load_trait_reference(t, compendium)
            for t in data["traits"]
        ],
        willpower=data["willpower"],
        strength=data["strength"],
        movement=data["movement"],
        attack=data["attack"],
        defense=data["defense"],
        special=data["special"],
        endurance=data["endurance"],
        ammunition=data["ammunition"],
        granted_weapon_id=data["granted_weapon_id"],
        compendium=compendium
    )