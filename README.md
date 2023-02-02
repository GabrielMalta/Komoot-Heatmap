# Komoot Heatmap

Draws a Leaflet-Heat heatmap over OpenStreetMaps of your komoot tours.

Allows automatic download of gpx files from komoot account.

## Instructions

1. Get your tour ids
    1. Go to your completed tours page (https://www.komoot.com/user/YOUR_USER_ID/tours?type=recorded)
    2. Scroll down until all tours are loaded
    3. Inspect the page (F12), right click \<html\> and "copy element"
    4. Paste page contents to a file named "tours.html"
2. Download your tours
    1. Configure your browser to download files without confirmation to the "gpx" folder
    2. Open an empty browser window, run "html2gpx.py", and quickly switch to the url bar
    3. Watch as the script automatically opens new tabs and downloads all your tours
    4. You may need to run "html2gpx.py" a couple times to ensure all files are correctly downloaded, especially if you have a lot of tours. The script only downloads files that have not been downloaded already
3. Generate the heatmap
    1. Run "gpx2leaflet.py"
4. View the results
    1. Open a terminal on the repo folder
    2. Run $ python3 -m http.server 8080
    3. Go to http://0.0.0.0:8080/webpage_leaflet/ on your browser

If you would prefer to download your tours manually, just place them in the "gpx" folder and skip steps 1 and 2.