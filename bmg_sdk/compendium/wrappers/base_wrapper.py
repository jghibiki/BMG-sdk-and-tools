
class BaseWrapper:
    def __init__(self, entities):
        self._entities = entities

    @property
    def all(self):
        return self._entities

    def find(self, id):
        for e in self._entities:
            if e.id == id:
                return e

    def filter(self, ids):
        return list(
            filter(
                lambda w: w.id in ids,
                self._entities
            )
        )
