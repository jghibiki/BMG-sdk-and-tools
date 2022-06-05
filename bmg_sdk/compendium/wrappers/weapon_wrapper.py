from typing import List
from bmg_sdk.compendium.wrappers.base_wrapper import BaseWrapper
from bmg_sdk.compendium.models.weapon import Weapon


class WeaponWrapper(BaseWrapper):
    def __init__(self, weapons: List[Weapon]):
        super().__init__(weapons)
