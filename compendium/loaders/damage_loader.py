from typing import Dict
from compendium.models.damage import Damage


def load_damage(data: Dict):
    if dict["damange_type_id"] == 0:
        blood = data["count"]
        stun = 0
    else:
        blood = 0
        stun = data["count"]
    return Damage(
        stun=stun,
        blood=blood
    )