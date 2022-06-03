
class TraitReference:
    def __init__(self,
                 trait_id: str,
                 alternate_name: str,
                 compendium: "Compendium"):
        self.id = trait_id
        self.alternate_name = alternate_name
        self._compendium = compendium

        self._trait = None

    def tait(self):
        if self._trait is None:
            self._trait = self._compendium.trait.get(self.id)
        return self._trait


class Trait:
    def __init__(self,
                 id: str,
                 name: str,
                 description: str,
                 compendium: "Compendium"):
        self.id = id
        self.name = name
        self.description = description
        self._compendium = compendium
