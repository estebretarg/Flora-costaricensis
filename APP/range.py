#Insert the elevation range of the specie as a python range value'0
import sys
import csv

def range_of_desired_numbers():
  #try:  
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
        #print(elevation_data)
        
        for i in range(0,len(elevation_data)):
          elevation_data[i] = int(elevation_data[i])

        x1 = elevation_data[0]
        y2 = elevation_data[1] + 1
        
        elevation = []
        for i in range(x1, y2):
          elevation.append(i)
        
        #print(type(elevation))
        #try:
          #write the records in a cvs file for further use.
          csv_writer = csv.writer(sys.stdout, delimiter =',')
          print(elevation)
          #csv_writer.writerows(elevation)

          #print("Los valores se guardaron correctamente")
        
        #except:  
          #print("Ha ocurrido un error")
        
        #print(elevation)

      elif respuesta == "No" or "no":
        print("Por favor ingrese los datos de nuevo")
        range_of_desired_numbers()

      else:
        print("Debe seleccionar Si o No")
        verify_data_input()
    
    verify_data_input()
  
  #except:
  #  print("Los valores deben ser numéricos")
    
range_of_desired_numbers()

