from typing import Dict
import requests

from compendium.loaders.trait_loader import load_trait
from compendium.loaders.weapon_loader import load_weapon
from compendium.models.compendium import Compendium
from compendium.loaders.affiliation_loader import load_affiliation
from compendium.loaders.character_loader import load_character
from compendium.loaders.equipment_loader import load_equipment
from compendium.wrappers.affiliation_wrapper import AffiliationWrapper


class CompendiumLoader:
    def __init__(self):
        self._raw_data = None

    def load(self):
        self._fetch_compendium_data()
        return self._build_compendium()

    def _fetch_compendium_data(self):
        response = requests.get("https://app.knightmodels.com/gamedata")

        if response.status_code != 200:
            print("Failed to fetch api data:".response.raw)
            exit(1)

        self._raw_data = response.json()

    def _build_compendium(self):

        compendium = Compendium()

        affiliations = [
            load_affiliation(a, compendium)
            for a in self._raw_data["affiliations"]
        ]

        characters = [
            load_character(c, compendium)
            for c in self._raw_data["characters"]
        ]

        equipment = [
            load_equipment(e, compendium)
            for e in self._raw_data["equipment"]
        ]

        traits = [
            load_trait(t, compendium)
            for t in self._raw_data["traits"]
        ]

        weapons = [
            load_weapon(w, compendium)
            for w in self._raw_data["weapons"]
        ]


        compendium._register_weapons(weapons)
        compendium._register_affiliations(affiliations)
        #compendium._register_upgrades(upgrades)
        compendium._register_characters(characters)
        compendium._register_equipment(equipment)

        return compendium
