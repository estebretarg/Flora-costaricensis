#Insert the elevation range of the specie as a python range value'0
import sys
import csv

def elevation_range():
  try:  
    print('Inserte el primer numero del rango de elevación')
    x = input()
    print('Ahora inserte el segundo numero del rango de elevación')
    y = input()
    
    def verify_data_input():
      print ("La elevación "+x+" - "+y+" es correcta? Si o No")
      respuesta = input()
      if respuesta == "Si":
        
        elevation_data = []
        elevation_data.append(x)
        elevation_data.append(y)
        
        #Convert str to int
        for i in range(0,len(elevation_data)):
          elevation_data[i] = int(elevation_data[i])

        #Creates a list with all values between the two elevation range given values.
        x1 = elevation_data[0]
        y1 = elevation_data[1] + 1
        
        elevation = []
        for i in range(x1, y1):
          elevation.append(i)
        
        #Convert int to str
        for i in range(0,len(elevation)):
          elevation[i] = str(elevation[i])
        
        try:
          #write the records in a cvs file for further use.
          csv_writer = csv.writer(sys.stdout, delimiter =',')
          #print ;'\n'.join('\t'.join(i) for i in elevation)
          csv_writer.writerow(elevation)
          
          with open('elevation_data.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(elevation)

          print("Los valores se guardaron correctamente")
        
        except:  
          print("Ha ocurrido un error")

      elif respuesta == "No" or "no":
        print("Por favor ingrese los datos de nuevo")
        elevation_range()

      else:
        print("Debe seleccionar Si o No")
        verify_data_input()
  
    verify_data_input()
  
  except:
    print("Los valores deben ser numéricos")
    
elevation_range()

