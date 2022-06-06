from dataclasses import dataclass
from math import floor

@dataclass
class Damage:
    def __init__(self, stun=0, blood=0):
        self.stun = stun
        self.blood = blood

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

    def __repr__(self):
        return f"Damage[stun={self.stun} blood={self.blood}]"
