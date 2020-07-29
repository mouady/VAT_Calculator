build_version = "v5"
import os
import csv
import time
import tkinter # This is for future tkinter interfaces
from configparser import ConfigParser #This id for save options (save fav coin , % favorite {?}, users)
config = ConfigParser()
# Codode for dinamic msg's
if os.name == "posix":
   delete_msg = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   delete_msg = "cls"

#---VERIFY AND CREATE CSV FILE---#
def create_csv():
  with open('old_calculations.csv', 'a', newline='') as file_csv: 
    data_row1 = (['Name Calculation', 'Coin', 'Gross price', '% VAT', 'Net price'])
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
 print ("    ¡Welcome to the VAT Calculator!")
 print ("----------------------------------------")
 print ("        What do you want to do?")
 print ("----------------------------------------")
 print ("Select an option:")
 print ("1: Calculate (With parameters)")
 print ("2: Calculate (Without parameters)")
 print ("3: Parameters")
 print ("4: Calculating History")
 print ("5: More information")
 print ("6: Show credits and version")
 print ("7: Exit")
 print ("----------------------------------------")
 options = int (input("Type the corresponding number of the option you want:"))
 os.system(delete_msg)
 
 if options == 1:
    config.read ("settings.ini")
    print("----------------------------------------")
    print("WARNING: DON'T TYPE SYMBOLS, ONLY NUMBERS")
    print("----------------------------------------")
    gross_price = float (input("Type the price of your product:"))

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
       coin_word = "pound"
       coin_symbol = "£"
    if coin == 5:
       coin_word = "Swiss franc"
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
    print (f"The net price of your product is: {net_price_comma}{coin_symbol}")
    print("----------------------------------------")
    calculation_name = str (input("How do you want to name this calculation?:"))
    
    values_csv = [calculation_name,coin_word,gross_price_comma,vat_comma,net_price_comma]
    
    if os.path.isfile("old_calculations.csv"):
       with open('old_calculations.csv', 'a', newline='') as file_csv: 
          _file = open('old_calculations.csv', 'a') 
          with _file:
             writer = csv.writer(file_csv) 
             writer.writerow(values_csv)
             
    print("----------------------------------------")
    print ("The calculation has been saved in the \ncalculation history successfuly")
    print("----------------------------------------")
    input("Press ENTER to accept")
    os.system(delete_msg)
    run_programe()

 if options == 2:
    print("----------------------------------------")
    print("WARNING: DON'T TYPE SYMBOLS, ONLY NUMBERS")
    print("----------------------------------------")
    time.sleep(1)
    os.system(delete_msg)
    print ("----------------------------------------")
    print (" What is the coin that you want to use?")
    print ("----------------------------------------")
    time.sleep(1)
    print ("1:Dolars ($)")
    print ("2:Euros (€)")
    print ("3:Yens (¥)")
    print ("4:Pounds (£)")
    print ("5:Swiss francs (Fr.)")
    print ("6:Pesos ($)")
    print ("7:Yuans (¥)")
    print ("----------------------------------------")
    coin = int (input("Type the corresponding number of the option you want:"))
    os.system(delete_msg)
    gross_price = float (input("Type the price of your product:"))
    vat = float (input("Type the percentage VAT of your country:"))

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
    print (f"The net price of your product is: {net_price_comma}{coin_symbol}")
    print("----------------------------------------")
    calculation_name = str (input("How do you want to name this calculation?:"))
    
    values_csv = [calculation_name,coin_word,gross_price_comma,vat_comma,net_price_comma]
    
    if os.path.isfile("old_calculations.csv"):
       with open('old_calculations.csv', 'a', newline='') as file_csv: 
          _file = open('old_calculations.csv', 'a') 
          with _file:
             writer = csv.writer(file_csv) 
             writer.writerow(values_csv)
             
    print("----------------------------------------")
    print ("The calculation has been saved in the \ncalculation history successfuly")
    print("----------------------------------------")
    input("Press ENTER to accept")
    os.system(delete_msg)
    run_programe()

 if options == 3:
    print("----------------------------------------")
    print ("Are you sure of change the parameters?")
    print("----------------------------------------")
    print ("The olds parameters will be deleted and you")
    print ("will type other new parameters ")
    print("----------------------------------------")

    print ("1: Yes")
    print ("2: No")
    print("----------------------------------------")
    salir = int (input("Type the corresponding number of the option you want:"))
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
    print ("This program is used to calculate what is the percentage of VAT \n that must be put on the products. This can be useful to self-employed.")
    print ("----------------------------------------")
    print ("----------------------------------------")
    input("Press ENTER to accept")
    os.system(delete_msg)
    run_programe()
 
 if options == 6:
     print ("----------------------------------------")
     print ("----------------------------------------")
     print ("The rights of this program are of:\n© 2020 Mohamed Ahmed")
     print (f"Build: {build_version}")
     print ("----------------------------------------")
     print ("----------------------------------------")
     input("Press ENTER to accept")
     os.system(delete_msg)
     run_programe()

 if options== 7:
    print ("----------------------------------------")
    print ("Are you sure to accept?")
    print ("1: Yes")
    print ("2: No")
    print ("----------------------------------------")
    salir = int (input("Type the corresponding number of the option you want:"))
    if salir == 1:
       exit()
    if salir == 2:
       os.system(delete_msg)
       run_programe()
    
 else:
    print ("----------------------------------------")
    print (f"Numbrer typed isn't valid \nReturning to the principal menu...")
    print ("----------------------------------------")
    time.sleep(1.5)
    os.system(delete_msg)
    run_programe()



run_programe()

 #UNUSED CODE
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
