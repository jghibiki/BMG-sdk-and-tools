# Batman Miniature Game SDK & Utils


## Scraper
Scrapes [this site](https://gilham.solutions/cards/1) for Batman Miniature Game character cards.

## TTS Sheet Generator

Generates a 10 x 7 card sheet set. The sheet sets can then
be uploaded to a hosting source, and then imported into Tabletop Simulator
using the [Custom Deck feature](https://kb.tabletopsimulator.com/custom-content/custom-deck/)

Special thanks to `Tobias1087` on the [Arkham Rejects Discord](https://discord.gg/WzZeWzcgua) for implementing the card 
renderer that makes this possible.


[Link to generated card sheets](https://drive.google.com/drive/folders/1QLG_V4D5yEktQPRdAHFSVNVBvVjaJXOX?usp=sharing)


### Importing the Sheets as Custom Decks in TTS
A note on importing the card sheets from Google Drive. The generated "sharable" link from google drive will not work 
with TTS. This is because the "sharable" link is actually to a web based image browser. To derive the URL needed for
TTS, get the image id from the sharable link:
e.g.
```
Sharable URL: https://drive.google.com/drive/folders/1QLG_V4D5yEktQPRdAHFSVNVBvVjaJXOX?usp=sharing
ID: 1QLG_V4D5yEktQPRdAHFSVNVBvVjaJXOX
```

Then the Id needs to be added to the end of this base url:
```
https://drive.google.com/uc?export=download&id=
```

### Updating Custom Decks in TTS:

*Note: this method should work for "Saved Objects" as well.*

1. Load an empty single player table
2. Open up the in-game options menu.
3. Uncheck "Mod Caching". This will require TTS to reach out to the hosting server to re-fetch the card sheets instead 
  of using cached copies.
4. Load the mod. (For saved objects, drag them onto the tabletop.) TTS should post a message that it is loading, and
  after a few moments the updated cards should load.
5. (Optional) Re-enable "Mod Caching" to avoid needing to re-download all assets whenever you load a game.

## Printable Card Generator

Generates `.docx` files containing the character cards in a 3.5" x 2.5" printable format. The docx files are grouped
by affiliation, meaning that some cards usable by multiple affiliations may be duplicated. 

The latest generated sheets can be found on [Google Drive](https://drive.google.com/drive/folders/1rOblle0vGKcGQrTGBC88SlWbJ21hlL58?usp=sharing).

## Updates

**2022/06/03**
- Adds compendium SDK for future use. The compendium sources its data from the api that backs the BMG app.
- Scrape operation skips id's that do not have actual characters by using the compendium sdk to know which character
    ids are valid.
- Scrape now detects when the character image is loaded instead of 4s for each character. This reducdes the scraping 
    time from 40 minutes to ~5 minutes depending on internet speeds.
- Updates the placement of cards on TTS sheets to ensure deterministic placement. The benefit of this is that if previously
    unused ids become used in the future, all other cards with an id greater than the new card will not be effected.
    This also means that the sheet can be updated without messing up TTS decks and saved objects.
- Adds `.docx` file generation.


<hr>

**Copyright Note:**

This project is unofficial and not endorsed by, or affiliated with Knight Models. All © belongs to Knight Models. Images and trademarks used without permission.
The link to their website is: https://www.knightmodels.com
