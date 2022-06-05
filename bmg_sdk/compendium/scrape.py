import requests


class Scraper:
    def __init__(self):
        self._compendium = None

    @property
    def compendium(self):
        if self._compendium is None:
            data = self._load_data()
            self._compendium = Compendium(data)
        return self._compendium

    def _load_data(self):
        response = requests.get("https://app.knightmodels.com/gamedata")

        if response.status_code != 200:
            print("Failed to fetch api data:".response.raw)
            exit(1)

        return response.json()



def main():

    c = Scraper().compendium

    for i in range(len(c.affiliations)):

        aff = c.affiliations[i]

        print(aff)
        print(aff.characters)
        print(aff.equipment)
        print("--------------------\n")


if __name__ == "__main__":
    main()

