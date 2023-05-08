import sqlite3
import os


## ------ PARA EJECUTAR EL SCRIPT Y VER SU FUNCION BORRAR LA DATABASE ------- ##

#Funcion que busca si la base de datos o archivos existen en nuestro Sistema Operativo
def check_db(filename):
    return os.path.exists(filename)

#Funcion que imprime todos el contenido de la tabla
def display_table(conn):
    #Crea cursor
    cursor = conn.cursor()
    #Selecciona todos los registros
    cursor.execute('select name, size, date from images;')
    #Selecciona fila por fila todos los valores
    for name, size, date in cursor.fetchall():
        #Los imprime
        print(name, size, date)


"""
#Variable para conectarse a la database
conn = sqlite3.connect('database.db')

#Para crear una database en la RAM directamente y no en el SO
conn = sqlite3.connect(':memory:')

#Creamos una ruta/nombre para el file
db_file = 'database.db'
#Creamos un alias de la funcion de sqlite para conectarse como conn
with sqlite3.connect(db_file) as conn:
    print('Created the connection!')
print('Automatically closed the connection!')

#Se crea un cursor virtual para navegar por la db
c = conn.cursor()
"""

db_file = 'database.db'
#Se crea un esquema de sql
schema_file = 'schema.sql'


#Comprueba con la funcion de check_db si existe la db, en caso de true se hace exit y no se crea
if check_db(db_file):
    print('Database already exists. Exiting...')
    exit(0)

#Se crea un alias de la funcion de open/read en rf
with open(schema_file, 'r') as rf:
    #Se crea una variable schema con la funcion y la funcion .read()
    schema = rf.read()

#Se crea un alias de la funcion de sqlite.connect en conn
with sqlite3.connect(db_file) as conn:
    print('Created the connection!')
    #Se ejecuta el script del schema_file en la que se crea la tabla y sus atributos name, size y date
    conn.executescript(schema)
    print('Created the Table! Now inserting')
    #Se ejecuta el script que se insertan los valores siguientes
    conn.executescript("""
                       insert into images (name, size, date)
                       values
                       ('sample.png', 100, '2019-10-10'),
                       ('ask_python.png', 450, '2019-05-02'),
                       ('class_room.jpeg', 1200, '2018-04-07');
                       """)
    print('Inserted values into the table!')
    #Se crea un cursor para tener un punto de referencia en la db
    cursor = conn.cursor()
    #Se ejecuta el script que selecciona todos los objetos de la tabla images
    cursor.execute("""
                      select * from images
                      """)
    #Se imprime a cada fila por fila, todos los registros y se imprime por pantalla sus valores
    for row in cursor.fetchall():
        name, size, date = row
        print(f'{name} {size} {date}')
print('Closed the connection!')

#Se crea otra variable para llamar a la database de la anterior por alguna razon
db_filename = 'database.db'

#Se crea un Alias de la función siguiente como conn1
with sqlite3.connect(db_filename) as conn1:
    print('Before changes:')
    #Con la función display_table se enseña todos el contenido de la tabla
    display_table(conn1)

    cursor1 = conn1.cursor()
    #Se inserta un valor en la tabla
    cursor1.execute("""
    insert into images (name, size, date)
    values 
    ('JournalDev.png', 2000, '2020-02-20');
    """)

    print('\nAfter changes in conn1:')
    display_table(conn1)

    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)

    # Commit from the first connection
    conn1.commit()
    print('\nAfter commit:')
    with sqlite3.connect(db_filename) as conn3:
        display_table(conn3)

    cursor1.execute("""
    insert into images (name, size, date)
    values ('Hello.png', 200, '2020-01-18');
    """)

    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)

    # Revert to changes before conn1's commit
    conn1.rollback()
    print('\nAfter connection 1 rollback:')
    with sqlite3.connect(db_filename) as conn4:
        display_table(conn4)