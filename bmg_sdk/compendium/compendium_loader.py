import requests

from bmg_sdk.compendium.loaders.trait_loader import load_trait
from bmg_sdk.compendium.loaders.weapon_loader import load_weapon
from bmg_sdk.compendium.models.compendium import Compendium
from bmg_sdk.compendium.loaders.affiliation_loader import load_affiliation
from bmg_sdk.compendium.loaders.character_loader import load_character
from bmg_sdk.compendium.loaders.equipment_loader import load_equipment


class CompendiumLoader:
    def __init__(self):
        self._raw_data = None
        self._compendium = None

    def load(self):
        if self._compendium is None:
            self._fetch_compendium_data()
            self._compendium = self._build_compendium()
        return self._compendium

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
