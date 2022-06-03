from typing import List
from compendium.wrappers.base_wrapper import BaseWrapper
from compendium.models.character import Character


class CharacterWrapper(BaseWrapper):
    def __init__(self, characters: List[Character]):
        super().__init__(characters)

        self._eternal = None
        self._non_eternal = None

    @property
    def eternal(self):
        if self._eternal is None:
            self._eternal = list(
                filter(
                    lambda e: e.eternal,
                    self._entities
                )
            )
        return self._eternal

    @property
    def non_eternal(self):
        if self._non_eternal is None:
            self._non_eternal = list(
                filter(
                    lambda e: not e.eternal,
                    self._entities
                )
            )
        return self._non_eternal
