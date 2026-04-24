import gpxpy
# import click
from tqdm import tqdm
import os

######################################### 
# MAIN
input_folder = "gpx/"
output_path = "webpage_leaflet/data.js"

with open(output_path, 'w') as output:
    print ("\nProcessing files...")
    output.write("const heat = L.heatLayer([\n")
    filenames = os.listdir(input_folder)
    # with click.progressbar() as bar:
        # for filename in bar:
    for filename in tqdm(filenames):

        #Verify file is a gpx file
        if not filename.lower().endswith(".gpx"):
            continue

        gpx_file = open(os.path.join(input_folder, filename))
        gpx = gpxpy.parse(gpx_file)

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    output.write("\t["+
                                    str(float(point.latitude))+
                                    ", "+
                                    str(float(point.longitude))+
                                    ",1],\n")
    output.write("], {radius: 5,blur: 10,maxZoom: 19}).addTo(map);")





