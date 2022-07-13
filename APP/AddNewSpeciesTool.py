# Is a tool to guide the user and add new species into the DB. In an easy way.

import sqlite3
import sys
import species_description
import elevation_range

# converts a file to binary for easy storage.
def file_to_binary(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertNewSpecieData():
    try:
        # DataBase connection and settings
        conn = sqlite3.connect('FloraCostaricensisDB.db')
        print("Conectado a la base de datos de FloraCostaricensis")
        # DataBase cursor
        cursor = conn.cursor()
         
        species_description.description
        file_to_binary(filename="description_data.csv")

        elevation_range
        file_to_binary(filename="elevation_data.csv")

    except:
        print("Ha ocurrido un error con la base de datos")
        exit