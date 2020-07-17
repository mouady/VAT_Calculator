build_version = "v5"
import os
import csv
import time
import tkinter # Esto es para las interfaces graficas
from configparser import ConfigParser #Esto es para guardar opciones en el futuro (guardar moneda , % favorito {?}, usuarios)
config = ConfigParser()
# Codigo para mensajes dinamicos 
if os.name == "posix":
   delete_msg = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   delete_msg = "cls"

#---VERIFICAR Y CREAR ARCHIVO CSV---#
def create_csv():
  with open('old_calculations.csv', 'a', newline='') as file_csv: #tener en cuenta newline
    data_row1 = (['Nombre Calculo', 'Moneda', 'Precio bruto', '% IVA', 'Precio neto'])
    _file = open('old_calculations.csv', 'a',) 
    with _file:
     writer = csv.writer(file_csv)
     writer.writerow(data_row1)

def check_csv():
  if os.path.isfile("old_calculations.csv"):
     pass
  else:
     create_csv()

check_csv() 
#---------------------------#

def run_programe():
 print ("----------------------------------------")
 print (" ¡Bienvenido a la calculadora del IVA!")
 print ("----------------------------------------")
 print ("           ¿Que desea hacer?")
 print ("----------------------------------------")
 print ("Seleccione una opción:")
 print ("1: Calcular (Con parametros)")
 print ("2: Calcular (Sin parametros)")
 print ("3: Parametros")
 print ("4: Historial")
 print ("5: Mas información")
 print ("6: Ver creditos y version")
 print ("7: Salir")
 print ("----------------------------------------")
 options = int (input("Escriba el numero correspondiente a lo que quiera hacer:"))
 os.system(delete_msg)
 
 if options == 1:
    config.read ("settings.ini")
    print("----------------------------------------")
    print("ADVERTENCIA: NO ESCRIBA SIMOLOS, SOLO NUMEROS")
    print("----------------------------------------")
    gross_price = float (input("Escriba cual es el precio su producto:"))

    vat = float (config["SETTINGS"]["f_vat"])
    tax = (gross_price*vat/100)
    net_price = (gross_price+tax)
    coin = int (config["SETTINGS"]["f_coin"])


    if coin == 1:
       coin_word = "Dolar"
       coin_symbol = "$"
    if coin == 2:
       coin_word = "Euro"
       coin_symbol = "€"
    if coin == 3:
       coin_word = "Yen"
       coin_symbol = "¥"
    if coin == 4:
       coin_word = "Libra"
       coin_symbol = "£"
    if coin == 5:
       coin_word = "Franco Suizo"
       coin_symbol = " Fr."
    if coin == 6:
       coin_word = "Peso"
       coin_symbol = "$"
    if coin == 7:
       coin_word = "Yuan"
       coin_symbol = "¥"

    gross_price_str = str (gross_price)
    net_price_str = str (net_price)
    vat_str = str (vat)
    gross_price_comma = gross_price_str.replace('.',',')
    net_price_comma = net_price_str.replace('.',',')
    vat_comma = vat_str.replace('.',',')

    print("----------------------------------------")
    print (f"El precio neto de su producto es de: {net_price_comma}{coin_symbol}")
    print("----------------------------------------")
    calculation_name = str (input("¿Como desea guardar este calculo?:"))
    
    values_csv = [calculation_name,coin_word,gross_price_comma,vat_comma,net_price_comma]
    
    if os.path.isfile("old_calculations.csv"):
       with open('old_calculations.csv', 'a', newline='') as file_csv: 
          _file = open('old_calculations.csv', 'a') 
          with _file:
             writer = csv.writer(file_csv) 
             writer.writerow(values_csv)
             
    print("----------------------------------------")
    print ("Calculo guardado en el historial con éxito")
    print("----------------------------------------")
    input("Presione ENTER para aceptar")
    os.system(delete_msg)
    run_programe()

 if options == 2:
    print("----------------------------------------")
    print("ADVERTENCIA: NO ESCRIBA SIMOLOS, SOLO NUMEROS")
    print("----------------------------------------")
    time.sleep(1)
    os.system(delete_msg)
    print ("----------------------------------------")
    print ("   ¿Cual es la moneda que va usar?")
    print ("----------------------------------------")
    time.sleep(1)
    print ("1:Dolares ($)")
    print ("2:Euros (€)")
    print ("3:Yenes (¥)")
    print ("4:Libras (£)")
    print ("5:Francos suizos (Fr.)")
    print ("6:Pesos ($)")
    print ("7:Yuanes (¥)")
    print ("----------------------------------------")
    coin = int (input("Escriba el numero correspondiente:"))
    os.system(delete_msg)
    gross_price = float (input("Escriba cual es el precio su producto:"))
    vat = float (input("Escriba cual es el porcentaje del IVA en su pais:"))

    if coin == 1:
       coin_word = "Dolar"
       coin_symbol = "$"
    if coin == 2:
       coin_word = "Euro"
       coin_symbol = "€"
    if coin == 3:
       coin_word = "Yen"
       coin_symbol = "¥"
    if coin == 4:
       coin_word = "Libra"
       coin_symbol = "£"
    if coin == 5:
       coin_word = "Franco Suizo"
       coin_symbol = " Fr."
    if coin == 6:
       coin_word = "Peso"
       coin_symbol = "$"
    if coin == 7:
       coin_word = "Yuan"
       coin_symbol = "¥"

    tax = (gross_price*vat/100)
    net_price = (gross_price+tax)
    

    gross_price_str = str (gross_price)
    net_price_str = str (net_price)
    vat_str = str (vat)
    gross_price_comma = gross_price_str.replace('.',',')
    net_price_comma = net_price_str.replace('.',',')
    vat_comma = vat_str.replace('.',',')
    print("----------------------------------------")
    print (f"El precio neto de su producto es de: {net_price_comma}{coin_symbol}")
    print("----------------------------------------")
    calculation_name = str (input("¿Como desea guardar este calculo?:"))
    
    values_csv = [calculation_name,coin_word,gross_price_comma,vat_comma,net_price_comma]
    
    if os.path.isfile("old_calculations.csv"):
       with open('old_calculations.csv', 'a', newline='') as file_csv: 
          _file = open('old_calculations.csv', 'a') 
          with _file:
             writer = csv.writer(file_csv) 
             writer.writerow(values_csv)
             
    print("----------------------------------------")
    print ("Calculo guardado en el historial con éxito")
    print("----------------------------------------")
    input("Presione ENTER para aceptar")
    os.system(delete_msg)
    run_programe()

 if options == 3:
    print("----------------------------------------")
    print ("¿Esta seguro de querer cambiar los parametros?")
    print("----------------------------------------")
    print ("Los parametros de antes se borraran y usted tendra")
    print ("que escribir otros nuevos.")
    print("----------------------------------------")

    print ("1: Si")
    print ("2: No")
    print("----------------------------------------")
    salir = int (input("Escriba el numero correspondiente a lo que quiera hacer:"))
    if salir == 1:
       os.system(delete_msg)
       os.system("parameters.py") 
    if salir == 2:
       os.system(delete_msg)
       run_programe()

    os.system(delete_msg)
    os.system("parameters.py") 


 if options == 4:
    os.system(delete_msg)
    os.system("record.py")
    

 if options == 5:
    print ("----------------------------------------")
    print ("----------------------------------------")
    print ("Este programa se usa para calcular cual es el porcentaje de IVA \nque se deben poner a los productos. Esto puede serle útil a autonomos.")
    print ("----------------------------------------")
    print ("----------------------------------------")
    input("Presione ENTER para aceptar")
    os.system(delete_msg)
    run_programe()
 
 if options == 6:
     print ("----------------------------------------")
     print ("----------------------------------------")
     print ("Los derechos reservados del programa son para:\n© 2020 Mohamed Ahmed")
     print (f"Build: {build_version}")
     print ("----------------------------------------")
     print ("----------------------------------------")
     input("Presione ENTER para aceptar")
     os.system(delete_msg)
     run_programe()

 if options== 7:
    print ("----------------------------------------")
    print ("¿Esta seguro de querer salir?")
    print ("1: Si")
    print ("2: No")
    print ("----------------------------------------")
    salir = int (input("Escriba el numero correspondiente a lo que quiera hacer:"))
    if salir == 1:
       exit()
    if salir == 2:
       os.system(delete_msg)
       run_programe()
    
 else:
    print ("----------------------------------------")
    print (f"Numero escrito no valido \nVolviendo al menu principal...")
    print ("----------------------------------------")
    time.sleep(1.5)
    os.system(delete_msg)
    run_programe()



run_programe()


'''
 -- LINEAS DE CODIGO QUE PUEDEN SER ÚTILES --
    print ("----------------------------------------")
    print ("Clave no valida, intentelo de nuevo")
    print ("----------------------------------------")

    key = str (input("Ingrese la clave del producto (Con guiones):"))

 -------------------------------------------------------

    build_version = "v1.2"
 key = str
 from verify_key import *
 check_key()
 print ("----------------------------------------")
 print ("Para empezar, necesitamos verificar su producto")
 key = str (input("Escriba la clave de producto (Con guiones):"))
 print ("----------------------------------------")

 -------------------------------------------------------------------------------

 build_version = "v2.0a"

 from verify_key import *
 print ("----------------------------------------")
 print ("Para empezar, necesitamos verificar su producto")
 key = str (input("Escriba la clave de producto (Con guiones):"))
 print ("----------------------------------------")
 check_key()

 if activate_key == True:
    iniciar_programa()

 if activate_key == False:
    cerrar_programa()


 "7VEFH8RSUYX3RMQ1" or "2EH3B4MX60UDI96O"or "R2EHOO6M1WQNH0K1"
 -------------------------------------------------------------------------------
 print ("----------------------------------------")
 print ("¡Bienvenido")
 print ("----------------------------------------")
 print ("----------------------------------------")
 print ("Antes de comenzar, necesitamos saber algunas")
 print ("cosas sobre las que usted prefiere.")
 print ("----------------------------------------")
 moneda_fav = (input("¿Cual es la moneda que va usar?:"))
 iva_fav = (input("¿Cual es el porcentaje de IVA que va usar?:"))
 print ("----------------------------------------") 
 print ("Gracias, si desea cambiar estos parametros,")
 print ("dirijase a la sección 'Parametros' ")
 print ("----------------------------------------") 
 print ("Iniciando programa...")
 iniciar_programa()
'''
