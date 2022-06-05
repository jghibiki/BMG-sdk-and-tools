from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bmg_sdk.compendium.models.compendium import Compendium
from tqdm import tqdm
from bmg_sdk.utils.common import Paths, get_sanitized_name, get_character_dir_name


class Scraper:
    delay = 5
    card_bg_div = "Card_card__39xAa"
    card_parent_div = "Card_characters__iuvFJ"

    def __init__(self, compendium: Compendium):
        self.browser = None
        self.compendium = compendium

    def setup_browser(self):
        self.browser = webdriver.Firefox()

    def _wait_for_card_background_element(self):
        (
            WebDriverWait(self.browser, Scraper.delay)
                .until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, Scraper.card_bg_div)
                )
            )
        )

    def _wait_for_card_image_to_load(self):
        self.browser.execute_async_script(f"""
            var done = arguments[0];
            var a = new Image;
            a.onload = () => done(true);
            a.src = document.getElementsByClassName( '{Scraper.card_bg_div}' )[0].style.backgroundImage.replace('url(\"', "").replace('\")', "")
        """)

    def _locate_image_elements(self, character):
        elem = self.browser.find_element(By.CLASS_NAME, Scraper.card_parent_div)

        name = get_sanitized_name(character)
        children = elem.find_elements(By.XPATH, "./*")
        front = children[0]
        back = children[1]

        return name, front, back

    def _generate_screenshots(self, character, front, back):
        output_dir = Paths.card_output / get_character_dir_name(character)
        output_dir.mkdir()

        front.screenshot(str(output_dir / "front.png"))
        back.screenshot(str(output_dir / "back.png"))

    def scrape(self):
        self.setup_browser()

        for character in tqdm(self.compendium.characters.all):
            self.browser.get(character.get_card_url())
            delay = 5

            try:
                # ensure div exists
                self._wait_for_card_background_element()

                # wait till image loads
                self._wait_for_card_image_to_load()

                # scrape parent element
                name, front, back = self._locate_image_elements(character)

                # generate screenshot
                self._generate_screenshots(character, front, back)

                print(f"Scraped {name}")
            except TimeoutException:
                print("Load took too long")
        self.browser.close()


