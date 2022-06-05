from compendium.models.affiliation import Affiliation
from compendium.models.character import Character


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