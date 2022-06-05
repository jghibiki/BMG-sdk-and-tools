from typing import List

from compendium.models.trait import TraitReference


class Equipment:
    def __init__(self,
                 id: str,
                 name: str,
                 description: str,
                 max_count: str,
                 funding: int,
                 reputation: int,
                 image: str,
                 banned_character_ids: str,
                 banned_crew_equipment_ids: List[int],
                 required_character_ids: List[int],
                 required_crew_character_ids: List[int],
                 required_rank_ids: List[int],
                 required_affiliation_ids: List[int],
                 weapon_ids: List[int],
                 traits: List[TraitReference],
                 willpower: int,
                 strength: int,
                 movement: int,
                 attack: int,
                 defense: int,
                 special: int,
                 endurance: int,
                 ammunition: int,
                 granted_weapon_id: int,
                 compendium: "Compendium"
                 ):

        self.id = id
        self.name = name
        self.description = description
        self.max_count = max_count
        self.funding = funding
        self.reputation = reputation
        self.image = image
        self._banned_character_ids = banned_character_ids
        self._banned_crew_equipment_ids = banned_crew_equipment_ids
        self._required_character_ids = required_character_ids
        self._required_crew_character_ids = required_crew_character_ids
        self._required_rank_ids = required_rank_ids
        self._required_affiliation_ids = required_affiliation_ids
        self._weapon_ids = weapon_ids
        self._traits = traits
        self.willpower = willpower
        self.strength = strength
        self.movement = movement
        self.attack = attack
        self.defense = defense
        self.special = special
        self.endurance = endurance
        self.ammunition = ammunition
        self._granted_weapon_ids = granted_weapon_id

    def __repr__(self):
        return f"Equipment[{self.name}]"

