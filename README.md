# Lunar Landing Navigator
NASA Space Apps Challenge 2026: Lunar Landing Site Navigator

Live demo: https://harshitachauhan2410.github.io/lunar-navigator/

## Run it
1. Open the folder in VS Code and install the Live Server extension.
2. Right-click index.html and choose Open with Live Server.

Optional Python tests: python -m unittest discover -s tests -t .

## First use
1. Pick a site, or type a latitude and longitude.
2. Choose a start date and mission length.
3. Read the chart: when the Sun and Earth are above the horizon.
4. Check Best landing windows, then the heatmap to see how a small change in date or latitude changes the result.

## Limitations
The Sun and Earth positions use an approximate model (about one degree). Terrain is one horizon angle, not real elevation data. Not for flight operations. See docs/LIMITATIONS.md.

## Docs
docs/METHODOLOGY.md, docs/DATA_SOURCES.md, docs/LIMITATIONS.md, CHANGELOG.md

## Credits
Moon imagery: NASA https://spaceplace.na .
sa.gov/all-about-the-moon/en/the-moon-near-side.en.jpg.
Landing regions: NASA https://svs.gsfc.nasa.gov/4720/

