from typing import List

from bmg_sdk.compendium.models.affiliation import Affiliation
from bmg_sdk.compendium.models.character import Character
from bmg_sdk.compendium.models.equipment import Equipment
from bmg_sdk.compendium.models.upgrade import Upgrade
from bmg_sdk.compendium.models.weapon import Weapon
from bmg_sdk.compendium.wrappers.affiliation_wrapper import AffiliationWrapper
from bmg_sdk.compendium.wrappers.character_wrapper import CharacterWrapper
from bmg_sdk.compendium.wrappers.upgrade_wrapper import UpgradeWrapper
from bmg_sdk.compendium.wrappers.weapon_wrapper import WeaponWrapper


class Compendium:
    def __init__(self):
        self._affiliation_wrapper = None
        self._weapons_wrapper = None
        self._upgrades_wrapper = None
        self._characters_wrapper = None
        self._equipment_wrapper = None

    def _register_affiliations(self, affiliations: List[Affiliation]):
        self._affiliation_wrapper = AffiliationWrapper(affiliations)

    @property
    def affiliations(self):
        return self._affiliation_wrapper

    def _register_weapons(self, weapons: List[Weapon]):
        self._weapons_wrapper = WeaponWrapper(weapons)

    @property
    def weapons(self):
        return self._weapons_wrapper

    def _register_upgrades(self, upgrades: List[Upgrade]):
        self._upgrade_wrapper = UpgradeWrapper(upgrades)

    @property
    def upgrades(self):
        return self._upgrades_wrapper

    def _register_characters(self, characters: List[Character]):
        self._characters_wrapper = CharacterWrapper(characters)

    @property
    def characters(self):
        return self._characters_wrapper

    def _register_equipment(self, equipment: List[Equipment]):
        self._equipment_wrapper = CharacterWrapper(equipment)

    @property
    def equipment(self):
        return self._equipment_wrapper


