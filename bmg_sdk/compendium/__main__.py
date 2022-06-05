from compendium_loader import CompendiumLoader

def main():
    compendium = CompendiumLoader().load()

    print(compendium.characters.all[0].get_card_url())



if __name__ == "__main__":
    main()