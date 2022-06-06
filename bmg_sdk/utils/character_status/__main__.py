from bmg_sdk.utils.character_status.config_parser import ConfigParser
from bmg_sdk.utils.character_status.status_builder import StatusBuilder
from bmg_sdk.utils.common import Paths


def main():
    Paths.create_output_dir()
    Paths.create_card_info_output_dir()
    config = ConfigParser("./card_info.yml").load()

    for character, config in config.items():
        StatusBuilder(character, config).build()




if __name__ == "__main__":
    main()
