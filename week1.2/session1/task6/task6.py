# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

music_database = {

    "The Royston Club": ["Shaking Hips and Crashing Cars", "Songs For The Spine"],
    "Wunderhorse": ["Cub", "Midas"],
    "Bleech 9:3" : ["Bleech 9:3", "Bleed"]



}


# Pretty-print the data structure
#pprint(music_database)

# Display details of one album recorded by a specific artist
print(music_database.get("Bleech 9:3"))