import PySimpleGUI as sg
from src.windows import pantalla_principal
from src.component import ingresar_venta
from src.component import ver_version
from src.handlers import ingresar_venta_handler

def start():
    """
    Lanza la ejecucion de la ventana
    """
    window = loop()
    window.close()
def loop():
    """
    Loop de la ventana de manu que capta los eventos al apretar las opciones
    """
    window = pantalla_principal.build()
    window["-TABLA_VENTAS-"].update(ingresar_venta_handler.leer_archivo())

    while True:
        event,values = window.read()

        if event in (sg.WIN_CLOSED, "Exit", "-exit", "Salir"):
            break
        if event == '-INGRESAR_VENTA-':
            ingresar_venta.start()    
            window["-TABLA_VENTAS-"].update(ingresar_venta_handler.leer_archivo())
            
        if event == '-VER_VERSION-':
            ver_version.start()

    return window