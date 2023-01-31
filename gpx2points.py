import gpxpy
import click
import os

######################################### 
# MAIN
input_folder = "gpx/"
output_path = "points.csv"

with open(output_path, 'w') as output:
    print ("\nProcessing files...")
    output.write("latitude,longitude\n")
    with click.progressbar(os.listdir(input_folder)) as bar:
        for filename in bar:
            if (filename.lower().endswith(".gpx")):
                #Verify file is a gpx file
                gpx_file = open(os.path.join(input_folder, filename))
                gpx = gpxpy.parse(gpx_file)
                for track in gpx.tracks:
                    for segment in track.segments:
                        for point in segment.points:
                            output.write(str(float(point.latitude))+","+str(float(point.longitude))+"\n")




