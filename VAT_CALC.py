import os
import time

long_msg = """
---------------------------------------------------------
Usted tendra 2 opciones para poder realizar
sus calculos en este programa.

1. CALCULAR (CON PARAMETROS)
- Esta opcion le permite poder realizar sus
  calculos sin tener que poner todo el rato
  la moneda y el porcentaje de IVA. Se usa
  los parametros que usted ingrese y se guarda
  la configuración para todos los calculos que haga.
  Le puede ser util si los calculos que usted requiere
  realizar son en una sola moneda y porcentaje de IVA

2. CALCULAR (SIN PARAMETROS)
- Esta opcion le permite realizar los calculos pero se
  le preguntara que moneda y porcentaje de IVA quiere
  usar al momento. Esto le puede ser util si los calculos
  que usted requiere hacer son diferentes la moneda y el 
  porcentaje de IVA todo el rato.

Independientemente de que opción elija, a continuacion
se le preguntara los parametros que usted desea, los puede
cambiar en cualquier momento en la seccion "Parametros"
-----------------------------------------------------------
"""

if os.name == "posix":
   delete_msg = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   delete_msg = "cls"

if os.path.isfile("settings.ini"):
    os.system("calculator.py")
else:
 print ("----------------------------------------------")
 print ("                ¡Bienvenido!")
 print ("----------------------------------------------")
 time.sleep(1.5)
 os.system(delete_msg)
 print ("----------------------------------------------")
 print ("Antes de comenzar, necesitamos saber algunas")
 print ("cosas sobre las que usted prefiere.")
 print ("----------------------------------------------")
 time.sleep(3)
 os.system(delete_msg)
 print (long_msg)
 input("Presione ENTER para aceptar")
 os.system(delete_msg)
 os.system ("parameters.py")    
 
