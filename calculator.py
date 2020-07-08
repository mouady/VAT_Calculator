build_version = "v5a1"
import os
import csv
import time
import tkinter # Esto es para las interfaces graficas
import json #Esto es para guardar opciones en el futuro (guardar moneda , % favorito {?}, usuarios)
from csv_commands import create_csv

# Codigo para mensajes dinamicos 
if os.name == "posix":
   delete_msg = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   delete_msg = "cls"


# Codigo para loanding...
def loanding_msg():
 time.sleep(0.5)
 print (".")
 time.sleep(0.5)
 os.system(delete_msg)
 print ("..")
 time.sleep(0.5)
 os.system(delete_msg)
 print ("...")
 time.sleep(0.5)


def first_boot():
 #---------------------------#
 #- VERIFICAR ARCHIVO JSON -#
 if os.path.isfile("settings.json"):
    pass
 else:
    settings = {
      "first_boot": "False",
      "favorite_coin": "",
      "favorite_vat": ""
   }

    with open("settings.json", 'w') as json_file:
       json.dump(settings, json_file)
 #---------------------------#
 
 #---VERIFICAR ARCHIVO CSV---#
 def check_csv():
  if os.path.isfile("old_calculations.csv"):
     pass
  else:
     create_csv()

 check_csv()
 #---------------------------#

def run_programe():
 print ("----------------------------------------")
 print ("¡Bienvenido a la calculadora del IVA!")
 print ("----------------------------------------")
 print ("¿Que desea hacer?")
 print ("----------------------------------------")
 print ("Seleccione una opción:")
 print ("1:Calcular")
 print ("2:Mas información")
 print ("3:Opciones avanzadas")
 print ("4:Ver creditos y version")
 print ("5:Salir")
 print ("----------------------------------------")
 options = int (input("Escriba el numero correspondiente a lo que quiera hacer:"))
 os.system(delete_msg)

 if options == 1:
    print("----------------------------------------")
    print("ADVERTENCIA: NO ESCRIBA SIMOLOS, SOLO NUMEROS")
    print("----------------------------------------")
    gross_price = float (input("Escriba cual es el precio su producto:"))
    vat = float (input("Escriba cual es el porcentaje del IVA en su pais:"))

    tax = (gross_price*vat/100)
    net_price = (gross_price+tax)
    coin = ("Euro")

    gross_price_str = str (gross_price)
    net_price_str = str (net_price)
    vat_str = str (vat)
    gross_price_comma = gross_price_str.replace('.',',')
    net_price_comma = net_price_str.replace('.',',')
    vat_comma = vat_str.replace('.',',')
    print("----------------------------------------")
    print (f"El precio neto de su producto es de: {net_price_comma}€")
    print("----------------------------------------")
    calculation_name = str (input("¿Como desea guardar este calculo?:"))
    
    values_csv = [calculation_name,coin,gross_price_comma,vat_comma,net_price_comma]
    
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
    print ("----------------------------------------")
    print ("----------------------------------------")
    print ("Este programa se usa para calcular cual es el porcentaje de IVA \nque se deben poner a los productos. Esto puede serle útil a autonomos.")
    print ("----------------------------------------")
    print ("----------------------------------------")
    input("Presione ENTER para aceptar")
    os.system(delete_msg)
    run_programe()

 if options == 3:
    os.system(delete_msg)
    os.system("advanced_options.py")
 
 if options == 4:
     print ("----------------------------------------")
     print ("----------------------------------------")
     print ("Los derechos reservados del programa son para:\n© 2020 Mohamed Ahmed")
     print (f"Build: {build_version}")
     print ("----------------------------------------")
     print ("----------------------------------------")
     input("Presione ENTER para aceptar")
     os.system(delete_msg)
     run_programe()

 if options== 5:
    print ("----------------------------------------")
    print ("¿Esta seguro de querer salir?")
    print ("1:Si")
    print ("2:No")
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


first_boot()
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
 print ("¡Bienvenido!)
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
