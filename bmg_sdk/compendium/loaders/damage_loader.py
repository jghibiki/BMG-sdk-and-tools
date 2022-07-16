from typing import Dict
from bmg_sdk.compendium.models.damage import Damage


def load_damage(data: Dict):
    if data["damage_type_id"] == 1:
        blood = data["count"]
        stun = 0
    else:
        blood = 0
        stun = data["count"]
    return Damage(
        stun=stun,
        blood=blood
    )