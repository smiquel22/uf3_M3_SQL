import sqlite3

#Se crea la conexion a la base de datos bd1.db; como no hemos creado ninguna antes se genera una automaticamente
#y mediante la variable nos podemos conectar
conexion = sqlite3.connect("bd1.db")

#Se intenta crear una tabla, si ya esta creada nos imprime el error
try:
    #Se ejecuta un script sql que crea la tabla
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")