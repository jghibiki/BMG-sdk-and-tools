import json

import seaborn as sns

from bmg_sdk.compendium.compendium_loader import CompendiumLoader
from bmg_sdk.utils.common import Paths, get_character_dir_name
from simulation import Simulation

sns.set_theme()

melee_effort_combos = [-3, -2, -1, 0, 1, 2, 3]
ranged_effort_combos = [0, -1, -2, -3]
defense = [0, 1, 2, 3, 4, 5, 6]

def main():
    compendium = CompendiumLoader().load()

    Paths.create_stats_output_dir()

    build_stats(compendium)


def build_stats(compendium):
    for c in compendium.characters.non_eternal:
        name = f"Character: {c.alias} ({c.name})"
        print(f"Simulating attacks for: {name}")
        data = {}

        for w in c.weapons:
            print(f"Weapon {w.name}")
            weapon_dist = {}

            for d in defense:
                dist = {}

                if w.rate_of_fire is None:
                    for efforts in melee_effort_combos:
                        damage = Simulation().simulate_melee(c, d, efforts)
                        dist[f"{efforts} efforts"] = calculate_probs(damage)

                else:
                    for efforts in ranged_effort_combos:
                        damage = Simulation().simulate_ranged(c, w, d, efforts=efforts)
                        dist[f"{efforts} efforts"] = calculate_probs(damage)

                weapon_dist[f"defense {d}"] = dist

            data[w.name] = weapon_dist

        name = get_character_dir_name(c)
        with open(Paths.stats_report_output / f"{name}.json", "w") as f:
            json.dump(data, f, indent=4)


def calculate_probs(damage):
    stats = {}
    total = 0
    for d in damage:
        if d not in stats:
            stats[d] = 0
        stats[d] += 1
        total += 1

    probs = []
    for d, v in stats.items():
        probs.append({
            "stun": d.stun,
            "blood": d.blood,
            "prob": v / total
        })

    return probs


if __name__ == "__main__":
    main()
