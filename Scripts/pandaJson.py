import pandas as pd  
import numpy as np
import sys
import json

def read(file):
    df = pd.read_csv(file,header =  None ,names=['codigo_cliente','calificacion','fecha'],usecols=[0,1,2])
    df_nan = pd.DataFrame(pd.isnull(df.calificacion))
    df_nan = df_nan[df_nan['calificacion'] == True]
    df_nan = df_nan.reset_index()

    movie_np = []
    id_pelicula = 4500

    for i,j in zip(df_nan['index'][1:],df_nan['index'][:-1]):
    # numpy approach
        temp = np.full((1,i-j-1), id_pelicula)
        movie_np = np.append(movie_np, temp)
        id_pelicula += 1

    # Account for last record and corresponding length
    # numpy approach
    last_record = np.full((1,len(df) - df_nan.iloc[-1, 0] - 1),id_pelicula)
    movie_np = np.append(movie_np, last_record)

    df = df[pd.notnull(df['calificacion'])]

    df['id_pelicula'] = movie_np.astype(int)
    df['codigo_cliente'] = df['codigo_cliente'].astype(int)
    d = [ 
        dict([
        (colname, row[i]) 
        for i,colname in enumerate(df.columns)
        ])
        for row in df.values
    ]
    toJson(d)

def toJson(data):
    with open("output" + '.json',"w") as f:
        f.write(json.dumps(data))

if __name__ == "__main__":
    file = sys.argv[1]
    read(file)
    