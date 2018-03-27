import csv 
import sys 
import json

name = sys.argv[1]
name = name.split(".")
name = name[0]

with open(sys.argv[1],'rb') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open(name + '.json', 'w') as f:
     json.dump(rows, f)