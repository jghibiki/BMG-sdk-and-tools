from typing import List
from compendium.wrappers.base_wrapper import BaseWrapper
from compendium.models.character import Character


class CharacterWrapper(BaseWrapper):
    def __init__(self, characters: List[Character]):
        super().__init__(characters)

