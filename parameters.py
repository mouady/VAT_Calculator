import os
import time
import modules
import VAT_CALC


def run_parameters():
    print("-----------------------------------------------")
    print("WARNING: DON'T TYPE SYMBOLS, ONLY NUMBERS")
    print("-----------------------------------------------")
    time.sleep(1.5)
    print("----------------------------------------")
    print(" What is the coin that you want to use?")
    print("----------------------------------------")
    time.sleep(1)
    print("1:Dollars($)")
    print("2:Euros (€)")
    print("3:Yens (¥)")
    print("4:Pounds (£)")
    print("5:Swiss francs (Fr.)")
    print("6:Pesos ($)")
    print("7:Yuan's (¥)")
    print("----------------------------------------")
    favorite_coin = modules.input_number(
        "Type the corresponding number of the option you want:",
        run_parameters,
        False)

    if favorite_coin > 7:
        modules.invalid_number(run_parameters)

    print("----------------------------------------")
    favorite_vat = modules.input_number(
        "Type the percentage VAT of your country:",
        run_parameters,
        True)

    if favorite_vat > 100:
        modules.invalid_number(run_parameters)

    # noinspection PyTypeChecker
    modules.config["SETTINGS"] = {
        "f_coin": favorite_coin,
        "f_vat": favorite_vat

    }

    with open("confg/settings.ini", "w") as configfile:
        modules.config.write(configfile)

    os.system(modules.delete_msg)
    print("----------------------------------------")
    print("          -PARAMETERS SAVED-")
    print("----------------------------------------")
    print("If you want to change this parameters,")
    print("go to the section 'Parameters' ")
    print("----------------------------------------")
    time.sleep(3)
    os.system(modules.delete_msg)
    VAT_CALC.run_calculator()
