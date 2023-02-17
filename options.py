from colorsLog import *
import systemApi

def selection(op):
    if op == '0':
        exit()
    elif op == '1':
        info()
    elif op== '2':
        print('Opción 2 seleccionada')
    elif op == '3':
        print('Opción 3 seleccionada')
    elif op == '4':
        print('Opción 3 seleccionada')
    else:
        print('Opción no válida')

def menu():
    systemApi.clear()
    log('Escriba el número de la opción que desea: ')
    log(
    """
    0: Salir
    1: Información del equipo
    2: Ver claves disponibles
    3: Ver detalles del equipo
    4: Activar Office
    5: Habilitar gpedit
    \n""")
    option = input('Número de la opción: ')
    selection(option)

def info():
    print('\n'*5)
    bluelog('Que tipo de información desea ver: ')
    log("""
    0: Volver
    1: Sistema (systeminfo)
    2: Red (ipconfig)
    3: Conecciones activas (netstat)

    autor: nf 
    """)
    op = input('Número de la opción: ')
    if op == '0':
        menu()
    if op == '1':
        systemApi.executeCmdCommandExternal('systeminfo')
        info()
    if op == '2':
        systemApi.executeCmdCommandExternal('ipconfig')
    if op == '3':
        systemApi.executeCmdCommandExternal('netstat')
        info()
    if op == '4':
        systemApi.enabledGpedit()
    else:
        info()