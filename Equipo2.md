# Integrantes
- David Benitez
- Efrain Gonzalez
- Mayerli López

# Objetivos logrados
Uno de los principales objetivos que se lograron fue cargar los archivos en la base de datos de MongoDB, para esto se utilizaron diferentes scripts tanto propios como compartidos por el otro grupo que trabajó con MongoDB.

A continuación se puede observar los resultados obtenidos después de la implementación de cada script.

+--------------+------------------------------------------+  
|  CsvToJson     | 5 horas, resultado fallido.            |  
+--------------+------------------------------------------+    
| PandasJson   | 9 horas, resultado fallido.  |              
+--------------+------------------------------------------+


# Problemas y errores encontrados

Nos dimos cuenta que a pesar de estar procesando bien el archivo para limpiar la data, al momento de iniciar la operacion de escribir el json,  se consumian todos los procesos de las maquinas utilizadas , hasta que los procesos se suicidaban

# ¿Cómo se solucionaron los problemas?

Gracias a los scripts que el equipo 4 nos compartio, pudimos limpiar y formatear el archivo combined_data_2.txt y asi poder montarlo a la base de datos
la coleccion movie_titles tomo menos de un segundo en subirse a la base de datos
la coleccion scores_2  tomo 35 min aprox en subirse a la base de datos.
Gracias al workbench o IDE Studio 3T se pudo realizar la subida de ambos archivos sin mayor complicaciones

# ¿Cómo no se solucionaron los problemas?
