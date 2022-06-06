from typing import Dict
from functools import reduce

from bmg_sdk.compendium.loaders.trait_loader import load_trait_reference
from bmg_sdk.compendium.models.damage import Damage
from bmg_sdk.compendium.models.weapon import RawWeapon
from bmg_sdk.compendium.loaders.damage_loader import load_damage


def load_weapon(data: Dict, compendium):
    _d = data["damage"]
    if len(_d):
        d = [load_damage(d) for d in _d]
        damage = reduce(lambda a, b: a + b, d)
    else:
        damage = Damage()

    return RawWeapon(
        id=data["id"],
        name=data["name"],
        rate_of_fire=data["rate_of_fire"],
        ammunition=data["ammunition"],
        damage=damage,
        traits=[
            load_trait_reference(t, compendium)
            for t in data["traits"]
        ]
    )