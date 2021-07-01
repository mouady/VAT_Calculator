import os
import modules
import VAT_CALC


def run_record():
    welcome_record_msg()
    options_record()


def welcome_record_msg():
    print("----------------------------------------")
    print("Select an option:")
    print("1: Show history")
    print("2: Delete history")
    print("3: Go back to the principal menu")
    print("----------------------------------------")


def options_record():
    r_options = modules.input_number(
        "Type the corresponding number of the option you want:",
        run_record,
        False)

    if r_options == 1:
        print("----------------------------------------")
        print("Opening history...")
        modules.open_file("log/calculation_log.csv")
        os.system(modules.delete_msg)
        print("----------------------------------------")
        print("The history has been open")
        print("----------------------------------------")
        input("Press ENTER to accept")
        os.system(modules.delete_msg)
        run_record()

    if r_options == 2:
        os.remove("log/calculation_log.csv")
        print("----------------------------------------")
        print("The history has been deleted successfully")
        print("----------------------------------------")
        input("Press ENTER to accept")
        os.system(modules.delete_msg)
        VAT_CALC.run_calculator()

    if r_options == 3:
        os.system(modules.delete_msg)
        VAT_CALC.run_calculator()

    else:
        modules.invalid_number(run_record)
