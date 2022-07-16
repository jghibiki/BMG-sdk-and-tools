from random import choice

from bmg_sdk.compendium.models.character import Character
from bmg_sdk.compendium.models.damage import Damage
from bmg_sdk.compendium.models.weapon import Weapon


class Simulation:
    die = [i+1 for i in range(6)]

    @staticmethod
    def _roll():
        return choice(Simulation.die)

    def _simulate(self,
                  iterations,
                  strength,
                  strength_dice,
                  attack,
                  defense,
                  efforts,
                  damage):
        recorded_hits = []
        attack_dice = attack + efforts
        for _ in range(iterations):
            strength_rolls = [self._roll() for _ in range(strength_dice)]
            strength_hits = sum([
                strength_roll > strength
                for strength_roll in strength_rolls
            ])

            hits = sum([
                self._roll() > defense
                for _ in range(attack_dice)
            ])

            blocks = sum([
                self._roll() > attack
                for _ in range(defense)
            ])

            unblocked_hits = max(hits - blocks, 0)

            total_hits = unblocked_hits + strength_hits

            if total_hits not in recorded_hits:
                recorded_hits.append(total_hits)
            else:
                recorded_hits.append(total_hits)

        return {
            Damage(damage.stun*value, damage.blood*value)
            for value in recorded_hits
        }

    def simulate_ranged(self, attacker: Character, weapon: Weapon, defense, efforts, iterations=1000):
        return self._simulate(
            iterations,
            attacker.strength,
            strength_dice=1,
            attack=weapon.rate_of_fire,
            defense=defense,
            efforts=efforts,
            damage=weapon.damage
        )

    def simulate_melee(self, attacker: Character, defense, efforts, iterations=1000):
        return self._simulate(
            iterations,
            attacker.strength,
            strength_dice=1,
            attack=attacker.attack,
            defense=defense,
            efforts=efforts,
            damage=Damage(stun=1)
        )



