from typing import List
from dataclasses import dataclass

from bmg_sdk.compendium.models.damage import Damage
from bmg_sdk.compendium.models.trait import TraitReference


@dataclass
class RawWeapon:
    id: str
    name: str
    rate_of_fire: int
    ammunition: int
    damage: Damage
    traits: List[TraitReference]




@dataclass
class Weapon:
    pass