import os
# Solucion build_version
print ("----------------------------------------")
print ("Seleccione una opción:")
print ("1:Ver historial")
print ("2:Borrar historial")
opciones_3 = int (input("Escriba el numero correspondiente a lo que quiera hacer:"))

if opciones_3 == 1:
 os.system ("old_calculations.csv")
 print ("Abriendo historial...")
if opciones_3 == 2:
 os.remove ("old_calculations.csv")
 print ("El historial ha sido eliminado con exito")
