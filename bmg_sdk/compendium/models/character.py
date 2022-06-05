from typing import List
import requests
from io import BytesIO

from compendium.enums.rank_type import RankType
from compendium.models.character_affiliation import CharacterAffiliation
from compendium.models.trait import TraitReference

try:
    from PIL import Image, ImageDraw
    pil_enabled = True
except:
    pil_enabled = False


class Character:
    def __init__(self,
                 id: int,
                 name: str,
                 alias: str,
                 affiliations: List[CharacterAffiliation],
                 rival_affiliations_ids: List[int],
                 rank_ids: List[int],
                 weapon_ids: List[int],
                 image: str,
                 background: str,
                 willpower: int,
                 strength: int,
                 movement: int,
                 attack: int,
                 defense: int,
                 special: int,
                 endurance: int,
                 reputation: int,
                 funding: int,
                 eternal: bool,
                 bases_size: List[str],
                 traits: List[TraitReference],
                 upgrade_ids: List[int],
                 compendium: "Compendium"
                 ):
        self.id = id
        self.name = name
        self.alias = alias
        self.affiliations = affiliations
        self._affiliation_ids = list(map(lambda e: e.id, affiliations))
        self._rival_affiliation_ids = rival_affiliations_ids
        self.ranks = [RankType(r) for r in rank_ids]
        self._weapon_ids = weapon_ids
        self.image = image
        self.background = background
        self.willpower = willpower
        self.strength = strength
        self.movement = movement
        self.attack = attack
        self.defense = defense
        self.special = special
        self.endurance = endurance
        self.reputation = reputation
        self.funding = funding
        self.eternal = eternal
        self.bases_size = bases_size
        self.traits = traits
        self._upgrade_ids = upgrade_ids
        self._compendium = compendium

        self._rival_affiliations = None
        self._weapons = None
        self._upgrades = None

    @property
    def rival_affiliations(self):
        if self._rival_affiliations is None:
            self._rival_affiliations = list(
                filter(
                    lambda a: a.id in self._rival_affiliation_ids,
                    self._compendium.affiliations.all
                )
            )
        return self._rival_affiliations

    @property
    def weapons(self):
        if self._weapons is None:
            self._weapons = self._compendium.weapons.filter(self._weapon_ids)
        return self._rival_affiliations

    @property
    def upgrades(self):
        if self._upgrades is None:
            self._upgrades = self._compendium.upgrades.filter(self._upgrade_ids)
        return self._rival_affiliations

    def __repr__(self):
        return f"Character[{self.alias} ({self.name})]"

    def _download_image(self, url) -> "PIL.Image":
        r = requests.get(url)
        stream = BytesIO(r.content)
        return Image.open(stream)

    def get_card_url(self):
        return f"https://gilham.solutions/cards/{self.id}"

    def has_affiliation(self, id):
        return id in self._affiliation_ids



