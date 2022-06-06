from bmg_sdk.compendium.models.character import Character
from bmg_sdk.utils.common import get_character_dir_name, Paths


def character_card_paths(c: Character):
    card_dir = Paths.card_output / get_character_dir_name(c)

    front = (card_dir / "front.png")
    back = (card_dir / "back.png")
    return front, back
