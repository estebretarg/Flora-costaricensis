import sqlite3

conn = sqlite3.connect('FloraCostaricensisDB.db')

# Create a cursor
cursor = conn.cursor()

# create a table
cursor.execute(
    "INSERT INTO especies VALUES('Pinaceae', 'Pinus', 'Pinus caribea')")

# Commit our command
conn.commit()

# Close our connection
conn.close()
