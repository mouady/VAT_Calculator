import os

print ("----------------------------------------")
print ("Seleccione una opción:")
print ("1:Ver historial")
print ("2:Borrar historial")
opciones_3 = int (input("Escriba el numero correspondiente a lo que quiera hacer:"))

if opciones_3 == 1:
 os.system ("old_calculations.csv")
 print ("Abriendo historial...")
 input("prompt:")
 os.system("calculator.py")

if opciones_3 == 2:
 os.remove ("old_calculations.csv")
 print ("El historial ha sido eliminado con exito")
 input ("prompt")
 os.system("calculator.py")

else:
 print ("Numero escrito no valido")
 input ("prompt:") 
 os.system("advanced_options.py")
