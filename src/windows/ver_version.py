import PySimpleGUI as sg
from src.consts import fonts

def build():
    sg.theme('DarkTeal6')

    layout = [
        [sg.Image('src/resources/images/PySimpleGUI_logo.png')],
        [sg.Text("Version 1.0", key="-VERSION-", font=(fonts.font_name, 25))],
        [sg.Text("Desarrollado por Diego Gaston Diaz", key="-DESARROLLADOR-")],
        [sg.Text("https://github.com/Gaston-Diaz/ProyectoFinal-Python")]   
    ]

    window = sg.Window("Acerca de", layout=layout, modal=True, keep_on_top=True, element_justification='c')
    return window