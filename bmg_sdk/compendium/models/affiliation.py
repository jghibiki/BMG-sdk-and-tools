from dataclasses import dataclass

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from compendium.models.compendium import Compendium

@dataclass
class Affiliation:
    def __init__(self,
                 id: int,
                 name: str,
                 image: str,
                 icon: str,
                 is_team: bool,
                 eternal: bool,
                 compendium: "Compendium"):
        self.id = int(id)
        self.name = name
        self.image = image
        self.icon = icon
        self.is_team = is_team
        self.eternal = eternal
        self._compendium = compendium

        self._characters = None
        self._all_characters = None
        self._equipment = None

    @property
    def characters(self):
        """
        Get all non-eteral characters with this affiliation
        :return:
        """
        if self._characters is None:
            self._characters = list(
                filter(
                    lambda c: c.has_affiliation(self.id) and not c.eternal, # TODO validate this
                    self._compendium.characters.all
                )
            )
        return self._characters

    @property
    def all_characters(self):
        """
        Get all characters with this affiliation including eternal characters
        :return:
        """
        if self._all_characters is None:
            self._all_characters = list(
                filter(
                    lambda c: c.has_affiliation(self.id),
                    self._compendium.characters.all
                )
            )
        return self._all_characters

    @property
    def equipment(self):
        if self._equipment is None:
            self._equipment = list(
                filter(
                    lambda e: self in e.affiliations, # TODO validate this
                    self._compendium.equipment.all
                )
            )

    def __repr__(self):
        return f"Affiliation[{self.name} {self.id}]"






