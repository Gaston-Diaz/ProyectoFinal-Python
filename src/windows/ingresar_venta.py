import PySimpleGUI as sg
from src.consts import fonts

def build():
    sg.theme('DarkTeal6')

    categorias = ["Almacen","Bazar","Limpieza","Electro","Perfumeria"]

    layout = [
        [sg.Text('Ingresar venta', font=(fonts.font_name,28))],
        [sg.HorizontalSeparator()],
        [sg.Text("Codigo",size=(15,1)), sg.Input(size=(10,1), key="-CODIGO-")],
        [sg.Text("Cantidad", size=(15,1)), sg.Spin(list(range(99999)),size=(10,1), key="-CANTIDAD-")],
        [sg.Text("Precio", size=(15,1)), sg.Input(size=(10,1), key="-PRECIO-")],
        [sg.Text("Categoria", size=(15,1)), sg.Combo(categorias,default_value=categorias[0], key="-CATEGORIAS-")],
        [sg.Input(key="-FECHA-", size=(15,1)), sg.CalendarButton("Fecha",close_when_date_chosen=True, target="-FECHA-")],
        [sg.Button("Guardar",size=(10,1), key="-GUARDAR-", bind_return_key=True)]

    ]

    window = sg.Window('Ingresar venta', layout=layout, font=(fonts.font_name,fonts.font_size),modal=True)
    return window