import sqlite3

# Connect the DB
conn = sqlite3.connect('FloraCostaricensisDB.db')
print("Connected to FloraCostaricensis data base")
# SQLite cursor
cursor = conn.cursor()

# create a table
def table_creator():
    print ("What is the table name?")
    tableName = input()
    command = """CREATE TABLE %s
                    (
                        Familia TEXT,
                        Genero TEXT,
                        Especie TEXT,
                        Nombres_comunes TEXT,
                        Descripcion BLOB,
                        Zona_de_vida TEXT,
                        Rango_Elevacion BLOB,
                        Vertiente TEXT,
                        Naturaleza TEXT,
                        Usos TEXT,
                    )
                    """ % tableName
    cursor.execute(command) 
    print("Table successfully added")
    cursor.close()

def table_deleter():
    print ("What is the table name?")
    tableName = input()
    command = "DROP TABLE %s" % tableName
    cursor.execute(command)

print("What do you want to do?")
print("""1. Create a table \n2. Delete a table""")
selection = input()
if selection == "1": 
    table_creator()
elif selection == "2":
    table_deleter()