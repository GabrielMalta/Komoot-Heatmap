# Komoot Heatmap

Downloads your Draws a [Leaflet-Heat](https://github.com/Leaflet/Leaflet.heat) heatmap of your [Komoot](https://www.komoot.com/) activities (or other gpx files) over [OpenStreetMaps](https://www.openstreetmap.org/). Now featuring automagical downloads using [komPYoot](https://github.com/matiyau/komPYoot/).

## Instructions

0. Clone the repo
1. `$ python -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
2. Download your activities 
    1. `$ python3 download_tours.py`
    2. Enter your komoot credentials
    3. Watch as the script automagically downloads all your recorded activities
3. Generate the heatmap
    1. `$ python3 gpx2leaflet.py`
4. View the results
    1. `$ python3 -m http.server 8080`
    3. Go to http://0.0.0.0:8080/webpage_leaflet/ on your browser

If you would prefer to download your tours manually (or possibly from a service other than Komoot), just place them in the "gpx" folder and skip step 2.
gpx2leaflet.py has not been tested with gpx from other apps, but should work.

## TO DO

1. sliders to control heatmap radius and blurring
