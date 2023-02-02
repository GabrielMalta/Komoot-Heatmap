import gpxpy
import click
import os

######################################### 
# MAIN
input_folder = "gpx/"
output_path = "webpage_leaflet/data.js"

with open(output_path, 'w') as output:
    print ("\nProcessing files...")
    output.write("var heat = L.heatLayer([\n")
    with click.progressbar(os.listdir(input_folder)) as bar:
        for filename in bar:
            if (filename.lower().endswith(".gpx")):
                #Verify file is a gpx file
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
    output.write("], {radius: 25}).addTo(map);")





