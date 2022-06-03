from typing import List
from compendium.models.affiliation import Affiliation, Affiliation
from compendium.models.character import Character
from compendium.models.equipment import Equipment

def enhance_affiliation(affiliation: Affiliation,
                        compendium: Compendium,
                        ) -> Affiliation:
    Affiliation(
        id=affiliation.id,
        name=affiliation.name,
        image=affiliation.image,
        icon=affiliation.icon,
        is_team=affiliation.is_team,
        eternal=affiliation.eternal,
        characters=[
            c for c: Character in all_characters if c.
        ]
    )