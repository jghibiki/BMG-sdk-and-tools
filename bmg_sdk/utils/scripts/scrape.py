from bmg_sdk.compendium.compendium_loader import CompendiumLoader
from bmg_sdk.utils.common import Paths
from bmg_sdk.utils.generators.docx_generator import DocxGenerator
from bmg_sdk.utils.generators.tts_deck_generator import TtsDeckGenerator
from bmg_sdk.utils.scraper.scraper import Scraper


def main():
    Paths.create_output_dir()

    print("Loading compendium")
    compendium = CompendiumLoader().load()

    print("Scrape cards")
    Scraper().scrape()

    print("Building TTS Deck Sheets")
    TtsDeckGenerator().generate()

    print("Building Printable Card Sheets")
    DocxGenerator().generate()


if __name__ == "__main__":
    main()