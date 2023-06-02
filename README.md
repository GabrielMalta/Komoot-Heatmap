# Komoot Heatmap

Draws a [Leaflet-Heat](https://github.com/Leaflet/Leaflet.heat) heatmap of your [Komoot](https://www.komoot.com/) tours (or other gpx files) over [OpenStreetMaps](https://www.openstreetmap.org/).

Allows automatic download of gpx files from your Komoot tour page.

## Instructions

1. Get your tour ids
    1. Go to your completed tours page (https://www.komoot.com/user/YOUR_USER_ID/tours?type=recorded)
    2. Scroll down until all tours are loaded
    ~~3. Inspect the page (F12), right click \<html\> and "copy element"~~
    ~~4. Paste page contents to a file named "tours.html" in the repo directory~~
    3. Ctrl+S to "Save as..." as HTML only to a file named tours.html in the repo directory
2. Download your tours
    1. Configure your browser to download files __without confirmation__ to the __"gpx"__ folder
    2. Open an empty browser window, run "html2gpx.py", and quickly switch to the url bar
    3. Watch as the script automatically opens new tabs and downloads all your tours
    4. You may need to run "html2gpx.py" a couple times to ensure all files are correctly downloaded, especially if you have a lot of tours. The script only downloads files that have not been downloaded already
    5. Reminder to undo step 1 otherwise you'll be confused as to where your other downloads are going
3. Generate the heatmap
    1. Run "gpx2leaflet.py"
4. View the results
    1. Open a terminal on the repo folder
    2. Run `$ python3 -m http.server 8080`
    3. Go to http://0.0.0.0:8080/webpage_leaflet/ on your browser

If you would prefer to download your tours manually, just place them in the "gpx" folder and skip steps 1 and 2.

gpx2leaflet.py has not been tested with gpx from other apps, but should work.

## TO DO

1. Figure out a more elegant way to download tours, ideally without using PyAutoGUI
