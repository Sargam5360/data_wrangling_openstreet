import pprint
import re
import codecs
import json
import collections
from collections import defaultdict

#import pymongo
import os
datadir = "sanantonio_texas.osm" #"C:\\Users/Sargam/Desktop/udacity/data_wrangling/"
datafile = "sanantonio_texas.osm"
san_data = os.path.join(datadir, datafile)



def audit_zipcode(invalid_zipcodes, zipcode):
    twoDigits = zipcode[0:2]
    
    if not twoDigits.isdigit():
        invalid_zipcodes[twoDigits].add(zipcode)
    
    elif twoDigits != 78:
        invalid_zipcodes[twoDigits].add(zipcode)
        
def is_zipcode(elem):
    return (elem.attrib['k'] == "addr:postcode")

def audit_zip(osmfile):
    osm_file = open(osmfile, "r")
    invalid_zipcodes = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_zipcode(tag):
                    audit_zipcode(invalid_zipcodes,tag.attrib['v'])

    return invalid_zipcodes

san_zipcode = audit_zip(san_data)


pprint.pprint(dict(san_zipcode))


def update_name(zipcode):
    testNum = re.findall('[a-zA-Z]*', zipcode)
    if testNum:
        testNum = testNum[0]
    testNum.strip()
    if testNum == "TX":
        convertedZipcode = (re.findall(r'\d+', zipcode))
        if convertedZipcode:
            if convertedZipcode.__len__() == 2:
                return (re.findall(r'\d+', zipcode))[0] + "-" +(re.findall(r'\d+', zipcode))[1]
            else:
                return (re.findall(r'\d+', zipcode))[0]

for street_type, ways in san_zipcode.iteritems():
    for name in ways:
        better_name = update_name(name)
        print name, "=>", better_name