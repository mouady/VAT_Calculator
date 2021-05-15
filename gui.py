import PySimpleGUI as sg
import modules

sg.theme('LightGreen6')  # Add a touch of color
# All the stuff inside your window.

layout = [[sg.Text('Welcome to VAT Calculator!')],
          [sg.Text(modules.long_msg)],
          [sg.Button('Continue'), sg.Button('Exit')]]


def new_window():
    layout2 = [[sg.Button('Option 1')],
               [sg.Button('Option 2')],
               [sg.Button('Option 3')],
               [sg.Button('Option 4')],
               [sg.Button('Option 5')],
               [sg.Button('Option 6')],
               [sg.Button('Option 7')]]
    window2 = sg.Window('VAT Calculator | ©2021 Mohamed Ahmed', layout2)

    window2.read()


# Create the Window
window = sg.Window('VAT Calculator | ©2021 Mohamed Ahmed', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Continue':  # if user closes window or clicks cancel
        new_window()
    if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
        break

window.close()
