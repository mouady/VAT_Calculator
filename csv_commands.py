build_version = "v5a1"
import os 
import csv

def create_csv():
 with open('old_calculations.csv', 'a', newline='') as archivo_csv: #tener en cuenta newline
    datos_fila1 = (['Nombre Calculo', 'Moneda', 'Precio bruto', '% IVA', 'Precio neto'])
    archivo = open('old_calculations.csv', 'a',) 
    with archivo:
     writer = csv.writer(archivo_csv)
     writer.writerow(datos_fila1)
