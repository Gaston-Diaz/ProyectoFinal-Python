import PySimpleGUI as sg

def build():
    sg.theme('SystemDefault')

    layout = []

    window = sg.Window("Sistema v1.0", layout=layout, resizable=True, finalize=True)
    return window