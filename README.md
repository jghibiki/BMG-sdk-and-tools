# Batman Miniature Game card to TTS Generator

Scrapes [this site](https://gilham.solutions/cards/1) for Batman Miniature Game charcter cards, and
generates a 10 x 7 card sheet set. The sheet sets can then
be uploaded to a hosting source, and then imported into Tabletop Simulator
using the [Custom Deck feature](https://kb.tabletopsimulator.com/custom-content/custom-deck/)

Special thanks to `Tobias1087` on the [Arkham Rejects Discord](https://discord.gg/WzZeWzcgua) for implementing the card 
renderer that makes this possible.


[Link to generated card sheets](https://discord.com/channels/446255654978715649/480222798816608257/979443599315968020)


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

<hr>

**Copyright Note:**

This project is unofficial and not endorsed by, or affiliated with Knight Models. All © belongs to Knight Models. Images and trademarks used without permission.
The link to their website is: https://www.knightmodels.com
