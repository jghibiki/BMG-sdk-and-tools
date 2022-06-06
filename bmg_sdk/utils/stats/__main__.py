from bmg_sdk.compendium.compendium_loader import CompendiumLoader
from simulation import Simulation
import json
from pprint import pprint
import seaborn as sns
from pandas import DataFrame
import matplotlib.pyplot as plt

sns.set_theme()

effort_combos = [
    (3, 0),
    (2, 0),
    (1, 0),
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
]

ranged_effort_combos = [0, 1, 2, 3]

def main():
    compendium = CompendiumLoader().load()

    data = {}

    for c in compendium.characters.non_eternal:
        name = f"Character: {c.alias} ({c.name})"
        print(f"Simulating attacks for: {name}")
        data[name] = {
            "melee": Simulation().simulate_melee(c, 4, 0, 0)
        }

        for w in c.weapons:
            if w.rate_of_fire is None:
                distributions = [
                    (
                        efforts[0] + efforts[1]*-1,
                        damage,
                    )
                for efforts in effort_combos
                for damage, count in sorted(
                        Simulation().simulate_melee(c, 4, efforts[0], defender_efforts=efforts[1]).items(),
                        key=lambda e: e[0]
                    )
                for _ in range(count)
                ]
            else:
                distributions = [
                    (
                            efforts * -1,
                            damage,
                    )
                    for efforts in ranged_effort_combos
                    for damage, count in sorted(
                        Simulation().simulate_ranged(c, w, defender_efforts=efforts).items(),
                        key=lambda e: e[0]
                    )

                    for _ in range(count)
                ]

            distributions = {
                "effort_offset" : list(map(lambda e: e[0], distributions)),
                "stun_damage": list(map(lambda e: e[1][0], distributions)),
                "blood_damage": list(map(lambda e: e[1][0], distributions)),
            }

            plot_data = DataFrame.from_dict(distributions)
            plot_data = plot_data.fillna(0)

            print(plot_data)
            sns.jointplot(data=plot_data, hue="effort_offset", x="stun_damage", y="blood_damage")
            plt.title(f"{name} {w.name}")
            plt.show(block=True)

            data[name][w.name] = distributions


    with open("stats.json", "w") as f:
        json.dump(data, f, indent=4)





if __name__ == "__main__":
    main()
