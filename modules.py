import os
import time
import csv
import configparser as cf
# import tkinter -> This is for future tkinter interfaces


build_version = "v6"

config = cf.ConfigParser()

if os.name == "posix":
    delete_msg = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    delete_msg = "cls"


def create_csv():
    with open('old_calculations.csv', 'a', newline='') as file_csv:
        data_row1 = (['Name Calculation', 'Coin', 'Gross price', '% VAT', 'Net price'])
        _file = open('old_calculations.csv', 'a', )
        with _file:
            writer = csv.writer(file_csv)
            writer.writerow(data_row1)


def check_csv():
    if os.path.isfile("old_calculations.csv"):
        pass
    else:
        create_csv()


def input_number(input_message: str, value_error_action: any, is_float: bool):
    try:
        if not is_float:
            dato = int(input(input_message))
        if is_float:
            dato = float(input(input_message))

        return dato
    except ValueError:
        os.system(delete_msg)
        print("----------------------------------------")
        print(f"You must type a number \nReturning back...")
        print("----------------------------------------")
        time.sleep(1.5)
        os.system(delete_msg)
        value_error_action()


def invalid_number(returning_action: any):
    os.system(delete_msg)
    print("----------------------------------------")
    print(f"Number typed isn't valid \nReturning to the principal menu...")
    print("----------------------------------------")
    time.sleep(1.5)
    os.system(delete_msg)
    returning_action()


long_msg = """
You will have 2 options to perform
your calculations in this program.

1. CALCULATE (WITH PARAMETERS)
- This option allows you to make your
  calculations without having to put all the time
  the currency and the VAT percentage. It's used
  the parameters that you enter and save
  the settings for all the calculations you do.
  It can be useful if the calculations you require
  perform are in a single currency and VAT percentage

2. CALCULATE (WITHOUT PARAMETERS)
- This option allows you to perform the calculations but
  will ask you what currency and VAT percentage you want
  use right away. This can be useful if you calculate
  that you need to do are the currency and the
  VAT percentage all the time.

Regardless of which option you choose, below
it will ask you the parameters that you want, you can
change at any time in the "Parameters" section
"""
