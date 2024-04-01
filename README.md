# DigitecScrapy

### How to use

Use this code to get details of a Digitec article on the console:

```python
from digitecScrapy import DigitecScrapy


digitecScrapy = DigitecScrapy()

article_number = 25048099
digitecScrapy.get_article_details_as_json(article_number, print_out=True, safe=True)
```

The print out looks like the following:

```bash
╔══════════════════════════════════════════════════════════════════════════════════╗
║ Article number:                         25048099                                 ║
║ Name:                                   GeForce RTX 4070 WINDFORCE OC 12G        ║
║ Brand:                                  Gigabyte                                 ║
║ Category                                Grafikkarte                              ║
║ Rating:                                 4.4                                      ║
║ Total Rating:                           73                                       ║
║ Total Questions:                        0                                        ║
║                                                                                  ║
║                                                                                  ║
║ Prices                                                                           ║
║ -------------------------------------------------------------------------------- ║
║ Galaxus                                 562 CHF                                  ║
║ orderflow.ch                            621.8 CHF                                ║
║ JACOB                                   678.15 CHF                               ║
║ technik-günstiger.de                    700.22 CHF                               ║
║                                                                                  ║
║                                                                                  ║
║ Availability Digitec                                                             ║
║ -------------------------------------------------------------------------------- ║
║ Mail:                                   oneday                                   ║
║ Zuerich:                                immediately                              ║
║ Lausanne:                               immediately                              ║
║ Basel:                                  immediately                              ║
║ Kriens:                                 halfday                                  ║
║ Winterthur:                             immediately                              ║
║ Bern:                                   immediately                              ║
║ Dietikon:                               immediately                              ║
║ St. Gallen:                             immediately                              ║
║ Genf:                                   halfday                                  ║
║ Wohlen:                                 immediately                              ║
║                                                                                  ║
║                                                                                  ║
║ Die wichtigsten Spezifikationen auf einen Blick                                  ║
║ -------------------------------------------------------------------------------- ║
║ Länge:                                  26.10 cm                                 ║
║ Anzahl Shaders:                         5888 x                                   ║
║ Grafikkarten Modell:                    RTX 4070                                 ║
║ Grafikspeichertakt:                     1.31 GHz                                 ║
║ Max. anschliessbare Monitore:           4 x                                      ║
║ Max. Videoauflösung:                    7680 x 4320 Pixels                       ║
║ Artikelnummer:                          25048099                                 ║
║                                                                                  ║
║                                                                                  ║
║ Allgemeine Informationen                                                         ║
║ -------------------------------------------------------------------------------- ║
║ Hersteller:                             Gigabyte Technology                      ║
║ Kategorie:                              Grafikkarte                              ║
║ Herstellernr.:                          GV-N4070WF3OC-12GD                       ║
║ Release-Datum:                          28.03.2023                               ║
║ Verkaufsrang in Kategorie Grafikkarte:  5 von 1831                               ║
║ Externe Links:                          Herstellerseite (de)                     ║
║                                                                                  ║
║                                                                                  ║
║ Grafikkarte Eigenschaften                                                        ║
║ -------------------------------------------------------------------------------- ║
║ Max. anschliessbare Monitore:           4 x                                      ║
║ PCI Express Version:                    4.0                                      ║
║ Max. Videoauflösung:                    7680 x 4320 Pixels                       ║
║ Steckkarte Formfaktor:                  3 Slots                                  ║
║                                                                                  ║
║                                                                                  ║
║ Grafikprozessor                                                                  ║
║ -------------------------------------------------------------------------------- ║
║ Grafikkarten Serie:                     nVidia GeForce                           ║
║ Grafikkarten Modell:                    RTX 4070                                 ║
║ Prozessor Taktfrequenz:                 2100 MHz                                 ║
║ Boost-Frequenz:                         2500 MHz                                 ║
║ Anzahl Shaders:                         5888 x                                   ║
║                                                                                  ║
║                                                                                  ║
║ Grafikspeicher                                                                   ║
║ -------------------------------------------------------------------------------- ║
║ Grafikspeichertyp:                      GDDR6X                                   ║
║ Speicherkapazität:                      12 GB                                    ║
║ Grafikspeichertakt:                     1.31 GHz                                 ║
║ Speicherschnittstelle:                  192 Bits                                 ║
║ Speicherbandbreite:                     504.20 GB/s                              ║
║                                                                                  ║
║                                                                                  ║
║ Kühlung Eigenschaften                                                            ║
║ -------------------------------------------------------------------------------- ║
║ Grafikkarte Kühlsystem:                 Aktiver Kühler                           ║
║ Anzahl Lüfter:                          3 x                                      ║
║                                                                                  ║
║                                                                                  ║
║ Grafikkarte Technologien                                                         ║
║ -------------------------------------------------------------------------------- ║
║ DirectX Version:                        12                                       ║
║ OpenGL Version:                         4.60                                     ║
║                                                                                  ║
║                                                                                  ║
║ Anschlüsse                                                                       ║
║ -------------------------------------------------------------------------------- ║
║ Video-Anschlüsse:                       DisplayPort (3x)                         ║
║ HDMI Version:                           2.10                                     ║
║ DisplayPort Version:                    1.4a                                     ║
║                                                                                  ║
║                                                                                  ║
║ Energieversorgung                                                                ║
║ -------------------------------------------------------------------------------- ║
║ Min. empfohlene Systemleistung:         650 W                                    ║
║ Strom Anschlüsse:                       8-pin ATX 12V                            ║
║                                                                                  ║
║                                                                                  ║
║ Produktdimensionen                                                               ║
║ -------------------------------------------------------------------------------- ║
║ Länge:                                  26.10 cm                                 ║
║ Breite:                                 14 cm                                    ║
║ Höhe:                                   5.80 cm                                  ║
║                                                                                  ║
║                                                                                  ║
║ Klimabeitrag                                                                     ║
║ -------------------------------------------------------------------------------- ║
║ CO₂-Emission:                                                                    ║
║ Klimabeitrag:                                                                    ║
║                                                                                  ║
║                                                                                  ║
║ Verpackungsdimensionen                                                           ║
║ -------------------------------------------------------------------------------- ║
║ Länge:                                  33.96 cm                                 ║
║ Breite:                                 22.88 cm                                 ║
║ Höhe:                                   8.73 cm                                  ║
║ Gewicht:                                1.23 kg                                  ║
║                                                                                  ║
║                                                                                  ║
║ Zutaten und Verwendungshinweise                                                  ║
║ -------------------------------------------------------------------------------- ║
║ Verwendungshinweise:                    2.                                       ║
╚══════════════════════════════════════════════════════════════════════════════════╝
```
