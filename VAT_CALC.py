import calculator
import os
import time
import modules
import parameters


def run_calculator():
    modules.check_csv()
    welcome_msg()
    menu_options()


def welcome_msg():
    print("----------------------------------------")
    print("    ¡Welcome to the VAT Calculator!")
    print("----------------------------------------")
    print("        What do you want to do?")
    print("----------------------------------------")
    print("Select an option:")
    print("1: Calculate (With parameters)")
    print("2: Calculate (Without parameters)")
    print("3: Parameters")
    print("4: Calculating History")
    print("5: More information")
    print("6: Show credits and version")
    print("7: Exit")
    print("----------------------------------------")


def menu_options():
    options = modules.input_number(
        "Type the corresponding number of the option you want:",
        run_calculator,
        False)

    os.system(modules.delete_msg)

    if options == 1:
        calculator.options_1()

    if options == 2:
        calculator.options_2()

    if options == 3:
        calculator.options_3()

    if options == 4:
        calculator.options_4()

    if options == 5:
        calculator.options_5()

    if options == 6:
        calculator.options_6()

    if options == 7:
        calculator.options_7()

    else:
        modules.invalid_number(run_calculator)


def run_vat():
    if os.path.isfile("confg/settings.ini"):
        run_calculator()

    else:
        print("----------------------------------------------")
        print("                  Welcome!")
        print("----------------------------------------------")
        time.sleep(1.5)
        os.system(modules.delete_msg)
        print("----------------------------------------------")
        print("Before starting, we need know things")
        print("which you prefer.")
        print("----------------------------------------------")
        time.sleep(3)
        os.system(modules.delete_msg)
        print(modules.long_msg)
        input("Press ENTER to accept")
        os.system(modules.delete_msg)
        parameters.run_parameters()


if __name__ == "__main__":
    run_vat()
