import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
import collections

datadir = "sanantonio_texas.osm" #"C:\\Users/Sargam/Desktop/udacity/data_wrangling/"
datafile = "sanantonio_texas.osm"
san_data = os.path.join(datadir, datafile)
#people invovlved in the map editing.
def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        for e in element:
            if 'uid' in e.attrib:
                users.add(e.attrib['uid'])
    return users
users = process_map(san_data)
len(users)