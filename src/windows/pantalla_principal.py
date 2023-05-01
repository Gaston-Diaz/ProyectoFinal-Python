import PySimpleGUI as sg
from src.consts import fonts

def build():
    sg.theme('DarkTeal6')

    layout = [
        [sg.Text("Compras", font=(fonts.font_name,20))],
        [sg.HorizontalSeparator()],
        [sg.Button("Ingresar compra", key="-INGRESAR_VENTA-", font=(fonts.font_name,11)), sg.Button("Acerca de", key="-VER_VERSION-", font=(fonts.font_name,11))],
        [sg.Table(values=[["-","-","-","-","-","-"]], key="-TABLA_VENTAS-",justification="c",
                  headings=[" Codigo ", "  Cantidad  "," Precio ", " Categoria ", " Fecha "],
                  row_height=20, num_rows=10)]
    ]

    window = sg.Window("Sistema de compras v1.0", layout=layout, resizable=True, finalize=True)
    return window