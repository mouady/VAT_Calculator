import os

if os.name == "posix":
   borrar_mensaje = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   borrar_mensaje = "cls"

print ("----------------------------------------")
print ("Seleccione una opción:")
print ("1:Ver historial")
print ("2:Borrar historial")
print ("3:Volver al menu principal")
print ("----------------------------------------")
opciones_3 = int (input("Escriba el numero correspondiente a lo que quiera hacer:"))

if opciones_3 == 1:
 print ("----------------------------------------")
 print ("Abriendo historial...")
 os.system ("old_calculations.csv")
 os.system(borrar_mensaje)
 print ("----------------------------------------")
 print ("El historial ha sido abierto")
 print ("----------------------------------------")
 input("Presione ENTER para aceptar")
 os.system(borrar_mensaje)
 os.system("advanced_options.py")
 

if opciones_3 == 2:
 os.remove ("old_calculations.csv")
 print ("----------------------------------------")
 print ("El historial ha sido eliminado con exito")
 print ("----------------------------------------")
 input("Presione ENTER para aceptar")
 os.system(borrar_mensaje)
 os.system("advanced_options.py")


if opciones_3 == 3:
 os.system(borrar_mensaje)
 os.system("calculator.py")





else:
 print ("Numero escrito no valido")
 print ("----------------------------------------")
 input("Presione ENTER para aceptar")
 os.system(borrar_mensaje)
 os.system("advanced_options.py")
 