import PySimpleGUI as sg
from src.consts import fonts

def build():
    sg.theme('DarkTeal6')

    layout = [
        
    ]

    window = sg.Window("Version 1.0", layout=layout, modal=True)