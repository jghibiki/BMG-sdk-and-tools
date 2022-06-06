from bmg_sdk.utils.character_status.config_parser import ConfigParser
from bmg_sdk.utils.character_status.status_builder import StatusBuilder
from bmg_sdk.utils.common import Paths
"""
Expected yaml format for card info:

character:
    round number:
        blood: int
        stun: int
        status:
        - list of statuses

Example:

harley quinn (the suicide squad):
  1:
    blood: 0
    stun: 0
    status:
  2:
    blood: 1
    stun: 3
    status:
      - KO
  3:
    blood: 7
    stun: 4
    status:
      - Casualty
deadshot (classic):
  1:
    blood: 0
    stun: 0
    status:
  2:
    blood: 7
    stun: 8
    status:
      - Casualty

"""


def main():
    Paths.create_output_dir()
    Paths.create_card_info_output_dir()
    config = ConfigParser("./card_info.yml").load()

    for character, config in config.items():
        StatusBuilder(character, config).build()


if __name__ == "__main__":
    main()
