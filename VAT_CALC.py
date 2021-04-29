import os
import time
import modules

if os.path.isfile("settings.ini"):
    os.system("calculator.py")
else:
    print("----------------------------------------------")
    print("                  Welcome!")
    print("----------------------------------------------")
    time.sleep(1.5)
    os.system(modules.delete_msg)
    print("----------------------------------------------")
    print("Before starting, we need know things")
    print("that you prefer.")
    print("----------------------------------------------")
    time.sleep(3)
    os.system(modules.delete_msg)
    print(modules.long_msg)
    input("Press ENTER to accept")
    os.system(modules.delete_msg)
    os.system("parameters.py")
