#Creates a .csv file to store de species description in order to add it to the data base
import csv

def description():
  try:
    text = []
    print("Por favor introduzca la descripción de la especie")
    d = input()
    text.append(d)

    with open('description_data.csv', 'w') as t:
            writer = csv.writer(t)
            writer.writerow(text)
  
  except:
    print("Ha ocurrido un error")

description()