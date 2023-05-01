import PySimpleGUI as sg
from src.windows import ingresar_venta
from src.handlers import ingresar_venta_handler

def start():

    window = loop()
    window.close()

def loop():
    window = ingresar_venta.build()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit", "-exit", "Salir"):
            break
        elif event == "-GUARDAR-":
            ingresar_venta_handler.agregar_venta(values)
            break
        
    return window