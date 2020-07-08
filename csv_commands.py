import os 
import csv

def create_csv():
 with open('old_calculations.csv', 'a', newline='') as file_csv: #tener en cuenta newline
    data_row1 = (['Nombre Calculo', 'Moneda', 'Precio bruto', '% IVA', 'Precio neto'])
    _file = open('old_calculations.csv', 'a',) 
    with _file:
     writer = csv.writer(file_csv)
     writer.writerow(data_row1)
