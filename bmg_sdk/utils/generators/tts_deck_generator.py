from PIL import Image

from bmg_sdk.utils.common import Paths, get_character_dir_name
from bmg_sdk.utils.scraper.util import character_card_paths


class TtsDeckGenerator:

    def __init__(self, compendium):
        Paths.create_sheet_output_dir()
        self.compendium = compendium

    @staticmethod
    def build_sheet(characters, sheet_number):
        # max tts supports
        w = 10
        h = 7

        sample_dir_name = Paths.card_output / get_character_dir_name(characters[0])

        (card_w, card_h) = Image.open(sample_dir_name / "front.png").size
        grid_size = (
            card_w * w,
            card_h * h
        )


        for c in characters:
            grid = Image.new("RGB", size=grid_size)

            front, back = character_card_paths(c)

            for side in ("front", "back"):
                card_path = front if side == "front" else back
                card_img = Image.open(card_path)
                relative_id = c.id - (70 * (sheet_number - 1))
                offset_x = (relative_id % w) * card_w
                offset_y = (relative_id // w) * card_h
                grid.paste(card_img, box=(offset_x, offset_y))

            output_file = Paths.sheet_output / f"sheet_{sheet_number}_{side}.png"
            grid.save(output_file)
            print(f"Exported sheet {sheet_number} - {side}")

    def generate(self):
        sheet_number = 1
        sheet = []

        # assign sheets by id, leaving blanks for spots that don't have a charracter with
        # matching id.
        for character in self.compendium.characters.all:
            if character.id // 70 != sheet_number - 1:
                self.build_sheet(sheet, sheet_number)
                sheet_number += 1
                sheet = []

            sheet.append(character)

