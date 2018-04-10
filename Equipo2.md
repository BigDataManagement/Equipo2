# PROYECTO 1 - Equipo 2<h1>
# Gestión de datos grandes <h2>


# Integrantes:
__Integrantes del equipo:__
* David Benitez
* Efrain Gonzalez
* Mayerli López

### Información del proyecto:
* __Equipo:__ #2
* __Motor de base de datos:__ MONGODB
* __IDE:__ Studio 3T for mongodb
* __Integración de datos:__ Pentaho: Data Integration

# Objetivos logrados<h2>
Uno de los principales objetivos que se lograron fue cargar los archivos en la base de datos de MongoDB, para esto se utilizaron diferentes scripts tanto propios como compartidos por el otro grupo que trabajó con MongoDB.

A continuación se puede observar los resultados obtenidos después de la implementación de cada script.

+--------------+------------------------------------------+  
|   CsvToJson     | 5 horas, resultado fallido.            |  
+--------------+------------------------------------------+    
| PandasJson   | 9 horas, resultado fallido.  |              
+--------------+------------------------------------------+

A pesar de que nuestros scripts fallaron, gracias a la colaboracion con el equipo 4 , logramos montar el archivo con la ayuda del workbench o IDE Studio 3T sin mayores complicaciones.


* la coleccion movie_titles tomo menos de un segundo en subirse a la base de datos
![](https://media.discordapp.net/attachments/429423569605492737/433118326676389888/unknown.png?width=860&height=484)

* la coleccion scores_2  tomo 35 min aprox en subirse a la base de datos.
![](https://media.discordapp.net/attachments/429423569605492737/433118378106945536/unknown.png?width=860&height=484)


* En las siguientes imágenes podemos ver la manera como se hace la consulta con las 5 mejores calificaciones.
![](https://cdn.discordapp.com/attachments/429423569605492737/433132959340691457/unknown.png)

* Y cuál fue el resultado obtenido.
![](https://cdn.discordapp.com/attachments/429423569605492737/433132897793343510/unknown.png)

* En la siguiente tabla podemos ver las calificaciones hechas a cada pelicula
![](https://cdn.discordapp.com/attachments/429423569605492737/433123964609363968/unknown.png)

* Los resultados obtenidos:
![](https://cdn.discordapp.com/attachments/429423569605492737/433137589063516160/unknown.png)

# Problemas y errores encontrados<h2>

*Nos dimos cuenta que a pesar de estar procesando bien el archivo para limpiar la data, al momento de iniciar la operacion de escribir el json,  se consumian todos los procesos de las maquinas utilizadas , hasta que los procesos se suicidaban.
*La realizacion de querys especificas en mongo se torno algo complicado para el equipo, por la poca experiencia con esta base de datos



# ¿Cómo se solucionaron los problemas?<h2>

Gracias a los scripts que el equipo 4 nos compartio, pudimos limpiar y formatear el archivo combined_data_2.txt y asi poder montarlo a la base de datos


# ¿Cómo no se solucionaron los problemas?
