import os
import configparser as cf
import time

if os.name == "posix":
   delete_msg = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   delete_msg = "cls"


def error_select():
   print ("----------------------------------------")
   print (f"Numbrer typed isn't valid \nReturning to the principal menu...")
   print ("----------------------------------------")
   time.sleep(1.5)
   os.system(delete_msg)
   os.system("parameters.py")

print ("-----------------------------------------------")
print ("WARNING: DON'T TYPE SYMBOLS, ONLY NUMBERS")
print ("-----------------------------------------------")
time.sleep(1.5)
print ("----------------------------------------")
print (" What is the coin that you want to use?")
print ("----------------------------------------")
time.sleep(1)
print ("1:Dolars($)")
print ("2:Euros (€)")
print ("3:Yens (¥)")
print ("4:Pounds (£)")
print ("5:Swiss francs (Fr.)")
print ("6:Pesos ($)")
print ("7:Yuans (¥)")
print ("----------------------------------------")
favorite_coin = int (input("Type the corresponding number of the option you want:"))

config = cf.ConfigParser()

if favorite_coin > 7:
     error_select()
 
print ("----------------------------------------")
favorite_vat = float (input("Type the percentage VAT of your country:"))

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
print ("          -PARAMETERS SAVED-") 
print ("----------------------------------------") 
print ("If you want to change this parameters,")
print ("go to the section 'Parameters' ")
print ("----------------------------------------")
time.sleep(3)
os.system(delete_msg) 
os.system ("calculator.py")