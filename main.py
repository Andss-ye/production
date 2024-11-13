from modules.fileManager import *

def menu():
    print('\n======== BIENVENIDO AL SISTEMA DE GESTIÓN DE PRODUCTOS ========')
    print('1. Registrar producto')
    print('2. Registrar materia prima')
    print('3. Listar productos')
    print('4. Listar materias primas')
    print('5. Salir del programa')
    opc = int(input('\nSeleccione su opcion: '))
    return opc

productos = loadData('db/productos.json')
opc = 10

while opc != 0:
    opc = menu()

    if opc == 1:
        print('registrar producto')

    elif opc == 2:
        print('registrar materia prima')

    elif opc == 3:
        print('listar productos')
    
    elif opc == 4:
        print('listar materias primas')

    elif opc == 0:
        print('Saliendo del programa...')
        exit()
    
    else:
        print('\nOpcion no valida, ingrese otra')
