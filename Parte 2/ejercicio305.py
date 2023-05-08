import sqlite3

conexion=sqlite3.connect("bd1.db")
#Creamos una variable cursor que implique seleccionar los atributos de la tabla articulos
#AKA: seleccionamos la fila entera
cursor=conexion.execute("select codigo,descripcion,precio from articulos")
#Recorremos con el select de toda la fila todos los registros ya que seleccionamos la fila y vamos saltando
#de 1 en 1 y printeamos
for fila in cursor:
    print(fila)
conexion.close()