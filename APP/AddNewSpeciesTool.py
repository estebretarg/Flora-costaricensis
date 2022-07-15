# Is a tool to guide the user and add new species into the DB. In an easy way.

import sqlite3

# converts a file to binary for easy storage.
def file_to_binary(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertNewSpecieData():
    try:
        # DataBase connection and settings
        conn = sqlite3.connect('FloraCostaricensisDB.db')

        # DataBase cursor
        cursor = conn.cursor()

        print("Digite el nombre de la familia")
        familia = input()

        print("Digite el género")
        genero = input()

        print("Digite el epíteto específico")
        epiteto = input()
        
        especie = genero + " " + epiteto

        print("Familia: "+familia+" Especie: "+genero+" "+ epiteto)

        import species_description
        species_description.description()
        descripcion = file_to_binary(filename="description_data.csv")

        print("Ingrese la o las zonas de vida para " + especie)
        zona_de_vida = [input()]

        import elevation_range
        elevation_range.elevation_range()
        elevacion = file_to_binary(filename="elevation_data.csv")

        print("Ahora indique la o las vertientes donde "+ especie +" se encuentra presente")
        vertiente = [input()]


        def insertData( Familia = familia, 
                        Genero = genero, 
                        Especie = especie, 
                        Descripcion = descripcion, 
                        Zona_de_vida = zona_de_vida, 
                        Elevacion = elevacion, 
                        Vertiente = vertiente):
            
            try:
                insertDataQuery = [Familia, Genero, Especie, Descripcion, Zona_de_vida, Elevacion, Vertiente]
                cursor.executemany("INSERT INTO Gimnospermas VALUES (?,?,?,?,?,?,?)", insertDataQuery)
                
                # Commit our command
                conn.commit()
                print("Data committed")
            
            except:
                print("error")
            
            finally:
                # Close our connection
                conn.close()
                print("Connection closed")

    except:
        print("Ha ocurrido un error con la base de datos")
        exit
    
    finally:
        exit

insertNewSpecieData()