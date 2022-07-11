import sqlite3
import numpy as np

conn = sqlite3.connect('FloraCostaricensisDB.db')

# Create a cursor
cursor = conn.cursor()

#Insert many inputs
especies_multiples = [
                        ('Meliaceae', 'Cedrela', 'Cedrela odorata'), 
                        ('Combretaceae', 'Terminalia', 'Terminalia amazonia')
                     ]

#create a table
#cursor.execute(
    #"""CREATE TABLE *name*(
    #   column 1 DATATYPE,
    #   column 2 DATATYPE
    # )""")

#Insert one input
#cursor.execute("INSERT INTO especies VALUES('x', 'y', 'z')")

#Insert many inputs
#cursor.executemany("INSERT INTO especies VALUES (?,?,?)", especies_multiples)

#Query the database
cursor.execute("SELECT rowid, * FROM especies")

lista = cursor.fetchall()

for sp in lista:
    print(sp)

#print(cursor.fetchall())

# Commit our command
conn.commit()

# Close our connection
conn.close()
