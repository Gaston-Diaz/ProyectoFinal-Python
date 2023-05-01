import PySimpleGUI as sg
from src.windows import ver_version

def start():
    window = loop()
    window.close()
def loop():
    window = ver_version.build()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit", "-exit", "Salir"):
            break
    return window