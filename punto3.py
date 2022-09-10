# 3.Construir un programa para ir de compras en un supermercado
# que permita la construcción del siguiente MENU:
# 1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
# 2. Digitar 2 para mostrar todos los productos registrados (+0.4)
# 3. Digitar 3 para permitir buscar por código un producto y editar el precio de este (+0.4)
# 4. Digitar 4 para permitir buscar por código un producto y eliminar el producto (+0.4)
# 5. Digitar 0 para SALIR
# Finalmente, versione y comparta el repositorio según las indicaciones dadas+(1.4)

print("BIENVENIDO")

eleccion = 0

productos = []
while eleccion != 5:

    print("*MENU SUPERMERCADO*")
    print("***")
    print("1. Agregar producto")
    print("2. Mostrar productos registrados")
    print("3. Buscar/Editar producto (buscar por código)")
    print("4. Buscar/Eliminar producto(buscar por código)")
    print("5. SALIR")

    producto = {}

    eleccion = int(input('Digite una opción del menú: '))

    if eleccion == 1:
      for i in range(1):
        producto['codigo'] = input('Digite el codigo del producto: ')
        producto['nombre'] = input('Digite el nombre del producto: ')
        producto['precio'] = float(input('Digite el precio del producto: '))

        productos.append(producto)
        print('Producto guardado exitosamente')

    elif (eleccion == 2):
      print(productos)

    elif (eleccion == 3):
        codigo = input('Ingrese el codigo del producto a buscar: ')

        producto = None
        encontrado = False

        for producto in productos:

            if producto['codigo'] == codigo:

                producto = producto
                encontrado = True
                break

        if encontrado:
          precioUpdate = float(
              input('Digite el precio del producto a editar: '))
          for i in producto:
            # if producto['precio'] ==
            producto['precio'] = precioUpdate
            # producto = { **producto, 'Precio': precioUpdate}
        print(producto)

    elif eleccion == 4:

        codigo = input('Ingrese el codigo del producto a eliminar: ')

        producto = None
        encontrado = False

        for producto in productos:

            if producto['codigo'] == codigo:

                producto = producto
                encontrado = True
                break

        if encontrado:

            productos.remove(producto)
            print(f'Se elimino el producto { codigo }')

        else:
          print(f'No existe el producto { codigo }')
    elif eleccion == 5:

        print('Gracias por usar el Menu del supermercado')
        break

    else:
        print("Digite una opcion correcta ")
else:
    print('Chao')


