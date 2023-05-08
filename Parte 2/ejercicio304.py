import sqlite3

#Creamos una variable para conectarnos a la bbdd
conexion=sqlite3.connect("bd1.db")
#Ejecutamos un script de insert sobre la tabla de articulos
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25))
#Aceptamos los cambios
conexion.commit()
#Cerramos la conexión
conexion.close()