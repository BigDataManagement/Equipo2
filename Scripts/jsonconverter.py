import csv 
import sys 
import json

# with open (sys.argv[1],'rb') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)
#with open('test.json','w') as f:
#    json.dump(rows,f)
# def read_csv(c_file,json_file):
#     csv_row = []
#     with open(c_file) as csvFile:
#         reader = csv.DictReader(csvFile)
#         title = reader.fieldnames
#         for row in reader:
#             csv_row.extend([{title[i]:row[title[i]]for i in range(len(title))}])
#         write_json(csv_row,json_file)

# def write_json(csv_file,json_file):
#     with open(json_file,'w') as f:
#         f.write(json.dumps(csv_file))
with open(sys.argv[1],'rb') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('movie_titles.json', 'w') as f:
    json.dump(rows, f)