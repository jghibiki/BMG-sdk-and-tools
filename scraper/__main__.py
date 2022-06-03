import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from shutil import rmtree
from pathlib import Path
from PIL import Image
from compendium.compendium_loader import CompendiumLoader
from tqdm import tqdm

output = Path("./output")
card_output = output / "cards"
sheet_output = output / "sheets"


def setup_browser():
    return webdriver.Firefox()


def sanitize_name(name):
    return name.replace(" ", "_").replace('"', "")


def scrape():
    browser = setup_browser()
    compendium = CompendiumLoader().load()

    for character in tqdm(compendium.characters.all):
        browser.get(character.get_card_url())
        delay = 5

        try:
            # ensure div exists
            (
                WebDriverWait(browser, delay)
                    .until(
                        EC.visibility_of_element_located(
                            (By.CLASS_NAME, "Card_card__39xAa")
                        )
                    )
            )

            # wait till image loads
            browser.execute_async_script("""
                var done = arguments[0];
                var a = new Image;
                a.onload = () => done(true);
                a.src = document.getElementsByClassName( 'Card_card__39xAa' )[0].style.backgroundImage.replace('url(\"', "").replace('\")', "")
            """)

            # scrape parent element
            elem = browser.find_element(By.CLASS_NAME, "Card_characters__iuvFJ")

            name = f"{character.alias}__{character.name}"
            sanitized_name = sanitize_name(name)
            children = elem.find_elements(By.XPATH, "./*")
            front = children[0]
            back = children[1]
            output_dir = card_output / f"{character.id}_{sanitized_name}"
            output_dir.mkdir()
            front.screenshot(str(output_dir / "front.png"))
            back.screenshot(str(output_dir / "back.png"))
            print(f"Scraped {name}")
        except TimeoutException:
            print("Load took too long")
    browser.close()
    exit(0)


def build_sheet(cards, sheet_number):
    # max tts supports
    w = 10
    h = 7

    (card_w, card_h) = Image.open(cards[0] / "front.png").size
    grid_size = (
        card_w * w,
        card_h * h
    )

    for side in ("front", "back"):
        grid = Image.new("RGB", size=grid_size)

        for i, card in enumerate(cards):
            card_img = Image.open(card / f"{side}.png")
            offset_x = (i % w) * card_w
            offset_y = (i // w) * card_h
            grid.paste(card_img, box=(offset_x, offset_y))

        output_file = sheet_output / f"sheet_{sheet_number}_{side}.png"
        grid.save(output_file)
        print(f"Exported sheet {sheet_number} - {side}")


def build_sheets():
    sheet_number = 1
    sheet = []

    for card in card_output.iterdir():
        sheet.append(card)

        if len(sheet) == 70:
            build_sheet(sheet, sheet_number)
            sheet_number += 1
            sheet = []

    if len(sheet) > 0:
        build_sheet(sheet, sheet_number)


def main():
    if output.exists():
        rmtree(output)

    output.mkdir()
    card_output.mkdir()
    sheet_output.mkdir()

    print("Scraping Cards")
    scrape()

    print("Building sheets")
    build_sheets()


if __name__ == '__main__':
    main()

