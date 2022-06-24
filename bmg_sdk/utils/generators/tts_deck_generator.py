import json
from PIL import Image

from bmg_sdk.utils.common import Paths, get_character_dir_name
from bmg_sdk.utils.scraper.util import character_card_paths


class TtsDeckGenerator:

    def __init__(self, compendium):
        #Paths.create_sheet_output_dir()
        self.compendium = compendium
        self.manifest = {}

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

        sheet_manifest = []

        for side in ("front", "back"):
            grid = Image.new("RGB", size=grid_size)

            for c in characters:
                print(c.alias)
                front, back = character_card_paths(c)

                card_path = front if side == "front" else back
                card_img = Image.open(card_path)
                id = c.id  # shift over 1 to use index 0 position
                relative_id = id - (70 * (sheet_number - 1))
                coord_x = (relative_id % w)
                coord_y = (relative_id // w)
                offset_x = coord_x * card_w
                offset_y = coord_y * card_h
                grid.paste(card_img, box=(offset_x, offset_y))

                if side == "front": # make sure we only do this once
                    sheet_manifest.append({
                        "id": c.id,
                        "name": f"{c.alias} - {c.name}",
                        "x": coord_x + 1, # tts decks are coordinate based starting at 1
                        "y": coord_y + 1,
                        "affiliations": list(
                            map(
                                lambda e: e.affiliation.name,
                                c.affiliations
                            )
                        )
                    })

            output_file = Paths.sheet_output / f"sheet_{sheet_number}_{side}.png"
            grid.save(output_file)
            print(f"Exported sheet {sheet_number} - {side}")
        return sheet_manifest

    def _add_sheet_manifest(self, sheet_number, sheet_manifest):
        self.manifest[sheet_number] = sheet_manifest

    def generate(self):
        sheet_number = 1
        sheet = []

        manifest = {}

        # assign sheets by id, leaving blanks for spots that don't have a character with
        # matching id.
        for character in sorted(self.compendium.characters.all, key=lambda el:el.id):
            if character.id // 70 != sheet_number - 1:
                manifest_entry = self.build_sheet(sheet, sheet_number)
                self._add_sheet_manifest(sheet_number, manifest_entry)
                sheet_number += 1
                sheet = []

            sheet.append(character)

        if len(sheet) > 0:  # cut last sheet
            manifest_entry = self.build_sheet(sheet, sheet_number)
            self._add_sheet_manifest(sheet_number, manifest_entry)

        with (Paths.sheet_output / "manifest.json").open("w") as f:
            m = {
                "cards": self.manifest,
                "affiliations": list(
                    map(
                       lambda e: e.name,
                        self.compendium.affiliations.all
                    )
                )
            }
            json.dump(m, f, indent=4)

