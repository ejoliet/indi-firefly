import PyIndi
import time
import sys, json
import threading
from astropy.io import fits

n=len(sys.argv)
print "Expecting first arg the config json file to test/parse=",n
print sys.argv
print(sys.argv[1])
#load configuration
json_text=open(sys.argv[1]).read()
config=json.loads(json_text)

print(config['star'])
print("RA, DEC of 'star'", config['star']['ra'], config['star']['dec'])
print(config['star']['name'])
