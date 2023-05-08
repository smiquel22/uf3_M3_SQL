import sqlite3

conexion=sqlite3.connect("bd1.db")
#Le pedimos al usuario que nos ingrese un input comparando que el precio sea menor que lo ingresado
precio=float(input("Ingrese un precio:"))
cursor=conexion.execute("select descripcion from articulos where precio<?", (precio, ))
#El cursor selecciona todas las filas
filas=cursor.fetchall()
#Imprime de todas las filas su descripción en caso de que cumpla la condicion que el precio sea menor al input
#del usuario, si no imprime un mensaje
if len(filas)>0:
    for fila in filas:
        print(fila)
else:
    print("No existen artículos con un precio menor al ingresado.")
conexion.close()