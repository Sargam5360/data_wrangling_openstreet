import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
import collections
#import pymongo
import os
datadir = "sanantonio_texas.osm" #"C:\\Users/Sargam/Desktop/udacity/data_wrangling/"
datafile = "sanantonio_texas.osm"
san_data = os.path.join(datadir, datafile)
#Parse through the file with ElementTree and count the number of unique element types to understand overall structure.
def count_tags(filename):
        tags = {}
        for event, elem in ET.iterparse(filename):
            if elem.tag in tags: 
                tags[elem.tag] += 1
            else:
                tags[elem.tag] = 1
        return tags
san_tags = count_tags(san_data)
pprint.pprint(san_tags)