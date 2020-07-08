import os

if os.name == "posix":
   delete_msg = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   delete_msg = "cls"

print ("----------------------------------------")
print ("Seleccione una opción:")
print ("1:Ver historial")
print ("2:Borrar historial")
print ("3:Volver al menu principal")
print ("----------------------------------------")
options_3 = int (input("Escriba el numero correspondiente a lo que quiera hacer:"))

if options_3 == 1:
 print ("----------------------------------------")
 print ("Abriendo historial...")
 os.system ("old_calculations.csv")
 os.system(delete_msg)
 print ("----------------------------------------")
 print ("El historial ha sido abierto")
 print ("----------------------------------------")
 input("Presione ENTER para aceptar")
 os.system(delete_msg)
 os.system("advanced_options.py")
 

if options_3 == 2:
 os.remove ("old_calculations.csv")
 print ("----------------------------------------")
 print ("El historial ha sido eliminado con exito")
 print ("----------------------------------------")
 input("Presione ENTER para aceptar")
 os.system(delete_msg)
 os.system("advanced_options.py")


if options_3 == 3:
 os.system(delete_msg)
 os.system("calculator.py")





else:
 print ("Numero escrito no valido")
 print ("----------------------------------------")
 input("Presione ENTER para aceptar")
 os.system(delete_msg)
 os.system("advanced_options.py")
 