from pathlib import Path
from shutil import rmtree

class Paths:
    output = Path("./output")
    card_output = output / "cards"
    sheet_output = output / "sheets"
    docx_output = output / "docx"

    @staticmethod
    def create_output_dir():
        if not Paths.output.exists():
            Paths.output.mkdir()

    @staticmethod
    def create_card_output_dir():
        Paths._create_dir(Paths.card_output)

    @staticmethod
    def create_sheet_output_dir():
        Paths._create_dir(Paths.sheet_output)

    @staticmethod
    def create_docx_output_dir():
        Paths._create_dir(Paths.docx_output)

    @staticmethod
    def _create_dir(path: Path):
        if path.exists():
            rmtree(path)
        path.mkdir()


def get_character_dir_name(character):
    name = get_sanitized_name(character)
    return f"{character.id}_{name}"


def get_sanitized_name(character):
    return (f"{character.alias}__{character.name}"
            .replace(" ", "_")
            .replace('"', "")
            )
