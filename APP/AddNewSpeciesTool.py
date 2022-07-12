#Is a tool to guide the user and add new species into the DB. In an easy way.

import sqlite3
import sys
import species_description
import elevation_range

# DataBase connection and settings
try:
    conn = sqlite3.connect('FloraCostaricensisDB.db')
    print("Conectado a la base de datos de FloraCostaricensis")
except:
    print("Ha ocurrido un error con la base de datos")

# DataBase cursor
cursor = conn.cursor()

species_description
elevation_range
