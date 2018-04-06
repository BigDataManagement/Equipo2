import sys, csv, json
#Read CSV File
def read_csv(file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        tem = "Nothing"
        for row in reader:
            if row['fecha'] is None:
                tem = row['id_cliente']
            else:
                csv_rows.extend([{'id_pelicula':tem, title[0]:row['id_cliente'], title[1]:row['calificacion'], title[2]:row['fecha']}])
        write_json(csv_rows)

#Convert csv data into json and write it
def write_json(data):
    with open("output" + '.json', "w") as f:
        f.write(json.dumps(data))

if __name__ == "__main__":
    file = sys.argv[1]
    read_csv(file)
