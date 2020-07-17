import os
import configparser as cf
import time

if os.name == "posix":
   delete_msg = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   delete_msg = "cls"


def error_select():
   print ("----------------------------------------")
   print (f"Numero escrito no valido \nIntentelo de nuevo...")
   print ("----------------------------------------")
   time.sleep(1.5)
   os.system(delete_msg)
   os.system("parameters.py")

print ("-----------------------------------------------")
print ("ADVERTENCIA: NO ESCRIBA SIMOLOS, SOLO NUMEROS")
print ("-----------------------------------------------")
time.sleep(1.5)
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
favorite_coin = int (input("Escriba el numero correspondiente a lo que quiera hacer:"))

config = cf.ConfigParser()

if favorite_coin > 7:
     error_select()
 
print ("----------------------------------------")
favorite_vat = float (input("¿Cual es el porcentaje de IVA que va usar?:"))

if favorite_vat > 100:
     error_select()
 
config["SETTINGS"] = {
 "f_coin" : favorite_coin ,
 "f_vat" : favorite_vat

 }

with open("settings.ini", "w") as configfile:
     config.write(configfile)

os.system(delete_msg)
print ("----------------------------------------") 
print ("        -PARAMETROS GUARDADOS-") 
print ("----------------------------------------") 
print ("Si desea cambiar estos parametros,")
print ("dirijase a la sección 'Parametros' ")
print ("----------------------------------------")
time.sleep(3)
os.system(delete_msg) 
os.system ("calculator.py")