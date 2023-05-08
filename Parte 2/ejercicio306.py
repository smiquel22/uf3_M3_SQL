import sqlite3

conexion=sqlite3.connect("bd1.db")
#Le preguntamos al usuario para que escriba un codigo de los registros
codigo=int(input("Ingrese el código de un artículo:"))
cursor=conexion.execute("select descripcion,precio from articulos where codigo=?", (codigo, ))
#Creamos la variable fila en un cursor el qual mediante el codigo nos imprimirá la fila del registro
#correspondiente, es decir, con código 1 imprimiremos el primer registro de la tabla
fila=cursor.fetchone()
if fila!=None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")
conexion.close()