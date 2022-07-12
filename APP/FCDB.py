import sqlite3


# Connect the DB
conn = sqlite3.connect('FloraCostaricensisDB.db')
print("Connected to FloraCostaricensis data base")
# SQLite cursor
cursor = conn.cursor()

# create a table


def table_creator():
    cursor.execute("""CREATE TABLE Gimnospermas
                    (
                        Familia TEXT,
                        Genero TEXT,
                        Especie TEXT,
                        Descripcion BLOB,
                        Zona_de_vida TEXT,
                        Altitud TEXT,
                        Vertiente TEXT
                    )
                    """)

# Convert sp description file to Binary in order to add it as BLOB DATATYPE into "description" column in table.


def file_to_binary(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(Familia, Genero, Especie, Descripcion, Zona_de_vida, Altitud, Vertiente):
        insert_blob_query = """
                            INSERT INTO Gimnospermas (Familia, Genero, Especie, Descripcion, Zona_de_vida, Altitud, Vertiente)
                            VALUES (?,?,?,?,?,?,?)

                            """
        print("Please enter the .txt file you want to convert")
        txt_file = str(input())
        file_binary = file_to_binary(txt_file)
        data_tuple = (Familia, Genero, Especie, file_binary,
                      Zona_de_vida, Altitud, Vertiente)
        # Commit our command
        conn.commit()
        print("Information committed")
    except

    finally:
        # Close our connection
        conn.close()
        print("Connection closed")


# Insert many inputs
Gimnospermas =  [
                    ('Cupressaceae', 
                    'Cupressus', 
                    'Cupressus lusitanica', 
                    [('Bosque humedo', 'Bosque muy humedo', 'Bosque pluvial')], 
                    '1000 - 1300', 'Pacifico')
                ]

# Insert many inputs
# cursor.executemany("INSERT INTO Gimnospermas VALUES (?,?,?,?,?,?,?)", Gimnospermas)


