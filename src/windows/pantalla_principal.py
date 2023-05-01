import PySimpleGUI as sg
from src.consts import fonts

def build():
    sg.theme('DarkTeal6')

    layout = [
        [sg.Text("Ventas del dia", font=(fonts.font_name,20))],
        [sg.HorizontalSeparator()],
        [sg.Button("Ingresar venta", key="-INGRESAR_VENTA-", font=(fonts.font_name,11)), sg.Button("Acerca de", key="-VERSION-", font=(fonts.font_name,11))],
        [sg.Table(values=[["-","-","-","-","-","-"]], key="-TABLA_VENTAS-",justification="c",
                  headings=[" Codigo ", "  Cantidad  "," Precio ", " Categoria ", " Fecha "],
                  row_height=20, num_rows=10)]
    ]

    window = sg.Window("Sistema v1.0", layout=layout, resizable=True, finalize=True)
    return window