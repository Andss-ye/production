def registrarProductos(productos):
    codigo = input('\nDigite el codigo del producto a registrar: ')
    nombre = input('Digite el nombre del producto: ')
    proveedor = input('Digite el proveedor del producto: ')

    if codigo not in productos:
        productos[codigo] = {
            'nombre': nombre,
            'proveedor': proveedor
        }
    
    else:
        print('El producto ya existe en el sistema.')
    
    return productos