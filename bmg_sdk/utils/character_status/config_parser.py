from pathlib import Path
import yaml


class ConfigParser:
    def __init__(self, path: str):
        self.config_path = Path(path)
        self._data = None

    def load(self):
        if self._data is None:
            self._data = self._load()
        return self._data

    def _load(self):
        return yaml.load(
            self.config_path.open("r"),
            Loader=yaml.Loader
        )
