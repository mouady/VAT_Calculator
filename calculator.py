build_version = "v5a1"
import os
import csv
import json #Esto es para guardar opciones en el futuro (guardar moneda , % favorito {?}, usuarios)
from csv_commands import create_csv

def primer_inicio():
 #---------------------------#
 #- VERIFICAR ARCHIVO JSON -#
 if os.path.isfile("settings.json"):
    pass
 else:
    ajustes = {
      "primer_inicio": "False",
      "moneda_favorita": "",
      "iva_favorito": ""
   }

    with open("settings.json", 'w') as archivo_json:
       json.dump(ajustes, archivo_json)
 #---------------------------#
 
 #---VERIFICAR ARCHIVO CSV---#
 def check_csv():
  if os.path.isfile("old_calculations.csv"):
     pass
  else:
     create_csv()

 check_csv()
 #---------------------------#

def iniciar_programa():
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
 opciones = int (input("Escriba el numero correspondiente a lo que quiera hacer:"))
 print ("----------------------------------------")


 if opciones == 1:
    print("----------------------------------------")
    print("ADVERTENCIA: NO ESCRIBA SIMOLOS, SOLO NUMEROS")
    print("----------------------------------------")
    precio_bruto = float (input("Escriba cual es el precio su producto:"))
    iva = float (input("Escriba cual es el porcentaje del IVA en su pais:"))

    impuesto = (precio_bruto*iva/100)
    precio_neto = (precio_bruto+impuesto)
    moneda = ("Euro")

    precio_bruto_str = str (precio_bruto)
    precio_neto_str = str (precio_neto)
    iva_str = str (iva)
    precio_bruto_coma = precio_bruto_str.replace('.',',')
    precio_neto_coma = precio_neto_str.replace('.',',')
    iva_coma = iva_str.replace('.',',')

    print (f"El precio neto de su producto es de: {precio_neto_coma}€")
    nombre_calculo = str (input("¿Como desea guardar este calculo?:"))
    
    valores_csv = [nombre_calculo,moneda,precio_bruto_coma,iva_coma,precio_neto_coma]
    
    if os.path.isfile("old_calculations.csv"):
       with open('old_calculations.csv', 'a', newline='') as archivo_csv: 
          archivo = open('old_calculations.csv', 'a') 
          with archivo:
             writer = csv.writer(archivo_csv) 
             writer.writerow(valores_csv)
    
    print ("Calculo guardado en el historial con éxito")
    print("----------------------------------------")
    input("prompt")
    iniciar_programa()


 if opciones == 2:
    print ("----------------------------------------")
    print ("Este programa se usa para calcular cual es el porcentaje de IVA \nque se deben poner a los productos. Esto puede serle útil a autonomos.")
    print ("----------------------------------------")
    print ("----------------------------------------")
    input ("prompt:")
    iniciar_programa()

 if opciones == 3:
    os.system("advanced_options.py")
 
 if opciones == 4:
     print ("----------------------------------------")
     print ("Los derechos reservados del programa son para:\n© 2020 Mohamed Ahmed")
     print (f"Build: {build_version}")
     print ("----------------------------------------")
     print ("----------------------------------------")
     input ("prompt:")
     iniciar_programa()

 if opciones== 5:
    print ("----------------------------------------")
    print ("¿Esta seguro de querer salir?")
    print ("1:Si")
    print ("2:No")
    salir = int (input("Escriba el numero correspondiente a lo que quiera hacer:"))
    if salir == 1:
       exit
    if salir == 2:
       iniciar_programa()
    
 else:
    print ("Numero escrito no valido")
    input ("prompt:") 
    iniciar_programa()


primer_inicio()
iniciar_programa()


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
