from typing import List
from bmg_sdk.compendium.models.affiliation import Affiliation
from bmg_sdk.compendium.wrappers.base_wrapper import BaseWrapper


class AffiliationWrapper(BaseWrapper):
    def __init__(self, affiliations: List[Affiliation]):
        super().__init__(affiliations)
        self._eternal = None
        self._non_eternal = None
        self._teams = None
        self._not_teams = None

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

    @property
    def teams(self):
        if self._teams is None:
            self._teams = list(
                filter(
                    lambda e: e.is_team,
                    self._entities
                )
            )
        return self._teams

    @property
    def not_teams(self):
        if self._not_teams is None:
            self._not_teams = list(
                filter(
                    lambda e: not e.is_team,
                    self._entities
                )
            )
        return self._not_teams

