import os

if os.name == "posix":
   delete_msg = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   delete_msg = "cls"

print ("----------------------------------------")
print ("Select an option:")
print ("1: Show history")
print ("2: Delete history")
print ("3: Go back to the principal menu")
print ("----------------------------------------")
r_options = int (input("Type the corresponding number of the option you want:"))

if r_options == 1:
 print ("----------------------------------------")
 print ("Opening history...")
 os.system ("old_calculations.csv")
 os.system(delete_msg)
 print ("----------------------------------------")
 print ("The history has been open")
 print ("----------------------------------------")
 input("Press ENTER to accept")
 os.system(delete_msg)
 os.system("record.py")
 

if r_options == 2:
 os.remove ("old_calculations.csv")
 print ("----------------------------------------")
 print ("El history has been deleted succesfuly")
 print ("----------------------------------------")
 input("PPress ENTER to accept")
 os.system(delete_msg)
 os.system("calculator.py")


if r_options == 3:
 os.system(delete_msg)
 os.system("calculator.py")





else:
 print ("Numbrer typed isn't valid")
 print ("----------------------------------------")
 input("Press ENTER to accept")
 os.system(delete_msg)
 os.system("advanced_options.py")
 