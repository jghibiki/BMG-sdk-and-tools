from dataclasses import dataclass
from math import floor

@dataclass
class Damage:
    stun: int
    blood: int

    def __add__(self, other):
        if isinstance(other, Damage):
            return Damage(
                stun=self.stun + other.stun,
                blood=self.blood + other.blood
            )
        else:
            print("unknown type of damage add operation")

    def __sub__(self, other):
        if isinstance(other, Damage):
            return Damage(
                stun=max(self.stun - other.stun, 0),
                blood=max(self.blood - other.blood, 0)
            )
        else:
            print("unknown type of damage subtract operation")

    def __mul__(self, other):
        if isinstance(other, int):
            return Damage(
                stun=self.stun * other,
                blood=self.blood * other
            )
        if isinstance(other, float):
            return Damage(
                stun=floor(self.stun * other),
                blood=floor(self.blood * other)
            )
        else:
            print("unknown type of damage subtract operation")

