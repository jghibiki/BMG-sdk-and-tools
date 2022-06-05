from dataclasses import dataclass



@dataclass
class CharacterAffiliation:

    def __init__(self,
                 affiliation_id: int,
                 can_be_team_boss: bool,
                 always_team_boss: bool,
                 compendium: "Compendium"):
        self.id = int(affiliation_id)
        self.can_be_team_boss = can_be_team_boss
        self.always_team_boss = always_team_boss
        self._compendium = compendium

        self._affiliation = None

    @property
    def affiliation(self):
        if self._affiliation is None:
            self._affiliation = self._compendium.affiliations.get(self.id)
        return self._affiliation
