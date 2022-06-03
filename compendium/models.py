from typing import Dict
from unidecode import unidecode
from functools import reduce

class Affiliations:
    def __init__(self, ):

class Affiliation:
    def __init__(self, data: Dict, compendium):
        self.id = data["id"]
        self.name = data["name"]
        self.image = data["image"]
        self.icon = data["icon"]
        self.is_team = data["is_team"]
        self.eternal = data["eternal"]

        self.compendium = compendium

        self._characters = None
        self._equipment = None

    def __repr__(self):
        return f"Affiliation[{self.name}]"

    @property
    def characters(self):
        if self._characters is None:
            self._characters = list(
                filter(
                    lambda e: e.has_affiliation(self.id),
                    self.compendium.characters
                )
            )
        return self._characters

    @property
    def equipment(self):
        if self._equipment is None:
            self._equipment = list(
                filter(
                    lambda e: e.has_required_affiliation(self.id),
                    self.compendium.equipment
                )
            )
        return self._equipment


class CharacterAffiliation:
    def __init__(self, data: Dict, compendium):
        self.affiliation_id = data["affiliation_id"]
        self.can_be_team_boss = data["can_be_team_boss"]
        self.always_team_boss = data["always_team_boss"]
        self.affiliation = compendium.get_affiliation(self.affiliation_id)


class Card:
    def __init__(self, data: Dict, compendium):
        self.id = data["id"]
        self.name = data["name"]
        self.image = data["image"]
        self.objective_type_id = data["objective_type_id"]
        self.count = data["count"]
        self.affiliation_id = data["affiliation_id"]
        self.rank_ids = data["rank_ids"]
        self.required_character_ids = data["required_character_ids"]

    def __repr__(self):
        return f"Card[{self.name}]"


class TraitReference:
    def __init__(self, data: Dict, compendium):
        self.trait_id = data["trait_id"]
        self.alternate_name = data["alternate_name"]
        self.compendium = compendium

    def trait(self):
        return self.compendium.get_trait(self.trait_id)

    def __repr__(self):
        return f"TraitReference[{self.alternate_name if self.alternate_name else self.trait.name}]"

class Character:
    def __init__(self, data: Dict, compendium):
        self.id = data["id"]
        self.name = data["name"]
        self.alias = data["alias"]
        self.affiliations = [
            CharacterAffiliation(a, compendium)
            for a in data["affiliations"]
        ]
        self.rival_affiliation_ids = data["rival_affiliation_ids"]
        self.rank_ids = data["rank_ids"]
        self.weapon_ids = data["weapon_ids"]
        self.image = data["image"]
        self.background = data["background"]
        self.willpower = data["willpower"]
        self.strength = data["strength"]
        self.movement = data["movement"]
        self.attack = data["attack"]
        self.defense = data["defense"]
        self.special = data["special"]
        self.endurance = data["endurance"]
        self.reputation = data["reputation"]
        self.funding = data["funding"]
        self.eternal = data["eternal"]
        self.bases_size = data["bases_size"]
        self.traits = [
            TraitReference(t, compendium)
            for t in data["traits"]
        ]
        self.upgrade_ids = data["upgrade_ids"]
        self.compendium = compendium

        self._weapons = None

    def __repr__(self):
        return f"Character[{self.name} | {self.alias}]"

    def has_affiliation(self, id):
        for a in self.affiliations:
            if a.affiliation_id == id:
                return True
        return False

    @property
    def weapons(self):
        if self._weapons is None:
            self._weapons = [
                self.compendium.get_weapon(w_id)
                for w_id in self.weapon_ids
            ]
        return self._weapons



class Equipment:
    def __init__(self, data: Dict, compendium):
        self.id = data["id"]
        self.name = data["name"]
        self.description = unidecode(data["description"]) if data["description"] else None
        self.max_count = data["max_count"]
        self.funding = data["funding"]
        self.reputation = data["reputation"]
        self.image = data["image"]
        self.banned_character_ids = data["banned_character_ids"]
        self.banned_crew_equipment_ids = data["banned_crew_equipment_ids"]
        self.required_character_ids = data["required_character_ids"]
        self.required_crew_character_ids = data["required_character_ids"]
        self.required_rank_ids = data["required_rank_ids"]
        self.required_affiliation_ids = data["required_affiliation_ids"]
        self.weapon_ids = data["weapon_ids"]
        self.traits = [
            TraitReference(t, compendium)
            for t in data["traits"]
        ]
        self.willpower = data["willpower"]
        self.strength = data["strength"]
        self.movement = data["movement"]
        self.attack = data["attack"]
        self.defense = data["defense"]
        self.special = data["special"]
        self.endurance = data["endurance"]
        self.ammunition = data["ammunition"]
        self.granted_weapon_id = data["granted_weapon_id"]

    def __repr__(self):
        return f"Equipment[{self.name}]"

    def has_required_affiliation(self, id):
        for affiliation_id in self.required_affiliation_ids:
            if affiliation_id == id:
                return True
        return False


class Trait:
    def __init__(self, data: Dict, compendium):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]

    def __repr__(self):
        return f"Trait[{self.name}]"


class Upgrade:
    def __init__(self, data: Dict, compendium):
        self.id = data["id"]
        self.rank_id = data["rank_id"]
        self.name = data["name"]
        self.bases_size = data["bases_size"]
        self.image = data["image"]
        self.willpower = data["willpower"]
        self.strength = data["strength"]
        self.movement = data["movement"]
        self.attack = data["attack"]
        self.defense = data["defense"]
        self.special = data["special"]
        self.endurance = data["endurance"]
        self.reputation = data["reputation"]
        self.funding = data["funding"]
        self.eternal = data["eternal"]
        self.weapon_ids = data["weapon_ids"]
        self.traits = [
            TraitReference(t, compendium)
            for t in data["traits"]
        ]

    def __repr__(self):
        return f"Upgrade[{self.name}]"


class Damage:
    def __init__(self, stun=0, blood=0):
        self.stun = stun
        self.blood = blood

    def from_dict(self, data: Dict):
        damage_type_id = data["damage_type_id"]

        if damage_type_id == 0:
            self.stun = data["count"]
            self.blood = 0
        else:
            self.stun = 0
            self.blood = data["count"]

        return self

    def __repr__(self):
        return f"Damage[stun={self.stun} blood={self.blood}]"

    def __add__(self, other):
        new = Damage(stun=self.stun, blood=self.blood)
        new.blood += other.blood
        new.stun += other.stun
        return new

    def __sub__(self, other):
        new = Damage(stun=self.stun, blood=self.blood)
        new.blood -= other.blood
        new.stun -= other.stun
        return new

    def __mul__(self, other):
        new = Damage(stun=self.stun, blood=self.blood)
        new.blood *= other
        new.stun *= other
        return new


class Weapons:
    def __init__(self, data: Dict, compendium):
        self.id = data["id"]
        self.name = data["name"]
        self.rate_of_fire = data["rate_of_fire"]
        self.ammunition = data["ammunition"]
        d = list(filter(
            lambda e: e is not None,
            [Damage().from_dict(d) for d in data["damage"]]
        ))
        if len(d) > 0:
            self.damage = reduce(lambda a, b: a + b, d)
        else:
            self.damage = Damage()

        self.traits = [
            TraitReference(t, compendium)
            for t in data["traits"]
        ]

    def __repr__(self):
        return f"Weapons[{self.name}]"


class Compendium:
    def __init__(self, data: Dict):
        self._affiliations = [
            Affiliation(a, self)
            for a in data["affiliations"]
        ]

        self._cards = [
            Card(c, self)
            for c in data["cards"]
        ]

        self._characters = [
            Character(c, self)
            for c in data["characters"]
        ]

        self._equipment = [
            Equipment(e, self)
            for e in data["equipment"]
        ]

        self._traits = [
            Trait(t, self)
            for t in data["traits"]
        ]

        self._updates = [
            Upgrade(u, self)
            for u in data["upgrades"]
        ]

        self._weapons = [
            Weapons(w, self)
            for w in data["weapons"]
        ]

        self._eternal = None
        self._non_eternal = None

    @property
    def eternal(self):
        if self._eternal is None:
            self._eternal = list(
                filter(
                    lambda e: e.eternal,
                    self.characters
                )
            )
        return self._eternal

    @property
    def non_eternal(self):
        if self._non_eternal is None:
            self._non_eternal = list(
                filter(
                    lambda e: not e.eternal,
                    self._characters
                )
            )
        return self._non_eternal

    def get_affiliation(self, id):
        for a in self._affiliations:
            if a.id == id:
                return a

    @property
    def affiliations(self):
        return list(
            filter(
                lambda e: not e.eternal,
                self._affiliations
            )
        )

    def get_character(self, id):
        for a in self._characters:
            if a.id == id:
                return a

    @property
    def characters(self):
        return list(
            filter(
                lambda e: not e.eternal,
                self._characters
            )
        )

    def get_equipment(self, id):
        for a in self._equipment:
            if a.id == id:
                return a

    @property
    def equipment(self):
        return self._equipment

    def get_trait(self, id):
        for a in self._traits:
            if a.id == id:
                return a

    def all_traits(self):
        return list(
            filter(
                lambda e: not e.eternal,
                self._traits
            )
        )

    def get_weapon(self, id):
        for w in self._weapons:
            if w.id == id:
                return w

