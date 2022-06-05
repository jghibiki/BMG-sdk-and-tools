from typing import List

from bmg_sdk.compendium.models.upgrade import Upgrade
from bmg_sdk.compendium.wrappers.base_wrapper import BaseWrapper


class UpgradeWrapper(BaseWrapper):
    def __init__(self, upgrades: List[Upgrade]):
        super().__init__(upgrades)

