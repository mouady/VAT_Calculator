import os
import csv
import time
import modules
import parameters
import VAT_CALC
import record


def options_1():
    modules.config.read("confg/settings.ini")
    print("----------------------------------------")
    print("WARNING: DON'T TYPE SYMBOLS, ONLY NUMBERS")
    print("----------------------------------------")
    gross_price = modules.input_number(
        "Type the price of your product:",
        VAT_CALC.run_calculator,
        True)

    vat = float(modules.config["SETTINGS"]["f_vat"])
    tax = (gross_price * vat / 100)
    net_price = (gross_price + tax)
    coin = int(modules.config["SETTINGS"]["f_coin"])

    if coin == 1:
        coin_word = "Dollar"
        coin_symbol = "$"
    if coin == 2:
        coin_word = "Euro"
        coin_symbol = "€"
    if coin == 3:
        coin_word = "Yen"
        coin_symbol = "¥"
    if coin == 4:
        coin_word = "pound"
        coin_symbol = "£"
    if coin == 5:
        coin_word = "Swiss franc"
        coin_symbol = " Fr."
    if coin == 6:
        coin_word = "Peso"
        coin_symbol = "$"
    if coin == 7:
        coin_word = "Yuan"
        coin_symbol = "¥"

    gross_price_str = str(gross_price)
    net_price_str = str(net_price)
    vat_str = str(vat)
    gross_price_comma = gross_price_str.replace('.', ',')
    net_price_comma = net_price_str.replace('.', ',')
    vat_comma = vat_str.replace('.', ',')

    print("----------------------------------------")
    print(f"The net price of your product is: {net_price_comma}{coin_symbol}")
    print("----------------------------------------")
    calculation_name = str(input("How do you want to name this calculation?:"))

    values_csv = [calculation_name, coin_word, gross_price_comma, vat_comma, net_price_comma]

    if os.path.isfile("log/calculation_log.csv"):
        with open('log/calculation_log.csv', 'a', newline='') as file_csv:
            _file = open('log/calculation_log.csv', 'a')
            with _file:
                writer = csv.writer(file_csv)
                writer.writerow(values_csv)

    print("----------------------------------------")
    print("The calculation has been saved in the \ncalculation history successfully")
    print("----------------------------------------")
    input("Press ENTER to accept")
    os.system(modules.delete_msg)
    VAT_CALC.run_calculator()


def options_2():
    print("----------------------------------------")
    print("WARNING: DON'T TYPE SYMBOLS, ONLY NUMBERS")
    print("----------------------------------------")
    time.sleep(1)
    os.system(modules.delete_msg)
    print("----------------------------------------")
    print(" What is the coin that you want to use?")
    print("----------------------------------------")
    time.sleep(1)
    print("1:Dollars ($)")
    print("2:Euros (€)")
    print("3:Yens (¥)")
    print("4:Pounds (£)")
    print("5:Swiss francs (Fr.)")
    print("6:Pesos ($)")
    print("7:Yuan's (¥)")
    print("----------------------------------------")
    coin = modules.input_number(
        "Type the corresponding number of the option you want:",
        VAT_CALC.run_calculator,
        False)

    os.system(modules.delete_msg)
    gross_price = modules.input_number(
        "Type the price of your product:",
        VAT_CALC.run_calculator,
        True)

    vat = modules.input_number(
        "Type the percentage VAT of your country:",
        VAT_CALC.run_calculator,
        True)

    if vat > 100:
        modules.invalid_number(VAT_CALC.run_calculator)

    if coin == 1:
        coin_word = "Dollar"
        coin_symbol = "$"
    if coin == 2:
        coin_word = "Euro"
        coin_symbol = "€"
    if coin == 3:
        coin_word = "Yen"
        coin_symbol = "¥"
    if coin == 4:
        coin_word = "Libra"
        coin_symbol = "£"
    if coin == 5:
        coin_word = "Swiss franc"
        coin_symbol = " Fr."
    if coin == 6:
        coin_word = "Peso"
        coin_symbol = "$"
    if coin == 7:
        coin_word = "Yuan"
        coin_symbol = "¥"

    tax = (gross_price * vat / 100)
    net_price = (gross_price + tax)

    gross_price_str = str(gross_price)
    net_price_str = str(net_price)
    vat_str = str(vat)
    gross_price_comma = gross_price_str.replace('.', ',')
    net_price_comma = net_price_str.replace('.', ',')
    vat_comma = vat_str.replace('.', ',')
    print("----------------------------------------")
    print(f"The net price of your product is: {net_price_comma}{coin_symbol}")
    print("----------------------------------------")
    calculation_name = str(input("How do you want to name this calculation?:"))

    values_csv = [calculation_name, coin_word, gross_price_comma, vat_comma, net_price_comma]

    if os.path.isfile("log/calculation_log.csv"):
        with open('log/calculation_log.csv', 'a', newline='') as file_csv:
            _file = open('log/calculation_log.csv', 'a')
            with _file:
                writer = csv.writer(file_csv)
                writer.writerow(values_csv)

    print("----------------------------------------")
    print("The calculation has been saved in the \ncalculation history successfully")
    print("----------------------------------------")
    input("Press ENTER to accept")
    os.system(modules.delete_msg)
    VAT_CALC.run_calculator()


def options_3():
    print("----------------------------------------")
    print("Are you sure about changing the parameters?")
    print("----------------------------------------")
    print("The olds parameters will be deleted and you")
    print("will type other new parameters ")
    print("----------------------------------------")

    print("1: Yes")
    print("2: No")
    print("----------------------------------------")
    exit_3 = modules.input_number(
        "Type the corresponding number of the option you want:",
        VAT_CALC.run_calculator,
        False)
    if exit_3 == 1:
        os.system(modules.delete_msg)
        parameters.run_parameters()
    if exit_3 == 2:
        os.system(modules.delete_msg)
        VAT_CALC.run_calculator()
    else:
        modules.invalid_number(VAT_CALC.run_calculator)

    os.system(modules.delete_msg)
    parameters.run_parameters()


def options_4():
    os.system(modules.delete_msg)
    record.run_record()


def options_5():
    print("----------------------------------------")
    print("----------------------------------------")
    print(
        "This program is used to calculate what is the percentage of VAT \n that must be put on the products. "
        "This can be useful to self-employed.")
    print("----------------------------------------")
    print("----------------------------------------")
    input("Press ENTER to accept")
    os.system(modules.delete_msg)
    VAT_CALC.run_calculator()


def options_6():
    print("----------------------------------------")
    print("----------------------------------------")
    print("The rights of this program are of:\n© 2020 Mohamed Ahmed")
    print(f"Build: {modules.build_version}")
    print("----------------------------------------")
    print("----------------------------------------")
    input("Press ENTER to accept")
    os.system(modules.delete_msg)
    VAT_CALC.run_calculator()


def options_7():
    print("----------------------------------------")
    print("Are you sure to accept?")
    print("1: Yes")
    print("2: No")
    print("----------------------------------------")
    exit_7 = modules.input_number(
        "Type the corresponding number of the option you want:",
        VAT_CALC.run_calculator,
        False)

    if exit_7 == 1:
        exit()
    if exit_7 == 2:
        os.system(modules.delete_msg)
        VAT_CALC.run_calculator()

    else:
        modules.invalid_number(VAT_CALC.run_calculator)
