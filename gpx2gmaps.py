import gpxpy
import click
import os

######################################### 
# MAIN
input_folder = "gpx/"
output_path = "webpage_gmaps/getPoints.js"

with open(output_path, 'w') as output:
    print ("\nProcessing files...")
    output.write("function getPoints() {\n\treturn [\n")
    with click.progressbar(os.listdir(input_folder)) as bar:
        for filename in bar:
            if (filename.lower().endswith(".gpx")):
                #Verify file is a gpx file
                gpx_file = open(os.path.join(input_folder, filename))
                gpx = gpxpy.parse(gpx_file)
                for track in gpx.tracks:
                    for segment in track.segments:
                        for point in segment.points:
                            output.write("\t\tnew google.maps.LatLng("+
                                         str(float(point.latitude))+
                                         ","+
                                         str(float(point.longitude))+
                                         "),\n")
    output.write("\t];\n}")





