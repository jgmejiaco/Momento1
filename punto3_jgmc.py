# 3.Construir un programa para ir de compras en un supermercado que permita la construcción del siguiente MENU:
#  1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
#  2. Digitar 2 para mostrar todos los productos registrados (+0.4)
#  3. Digitar 3 para permitir buscar por código un producto y editar el precio de este (+0.4)
#  4. Digitar 4 para permitir buscar por código un producto y eliminar el producto (+0.4)
#  5. Digitar 0 para SALIR
#  Finalmente, versione y comparta el repositorio según las indicaciones dadas+(1.4)

print("BIENVENIDO")

opcion = 5

productos = []

while (opcion != 0):
    print("MENÚ SUPERMERCADO")
    print("*****************")
    print("1. Agregar Producto")
    print("2. Mostrar todos los Productos")
    print("3. Buscar por Código un Producto y Editar el precio")
    print("4. Buscar por Código un Producto y Eliminar el producto")
    print("0. SALIR")
    print("*****************")

    producto = {}

    opcion = int( input ("Digite una opción: ") )

    if(opcion == 1):
        producto['codigo'] = input("Digite el código del producto: ")
        producto['nombre'] = input("Digite el nombre del producto: ")
        producto['precio'] = float( input("Digite el precio del producto: ") )

        productos.append(producto)
        print("Producto guardado existosamente")

    elif(opcion == 2):
        print(productos)

    elif(opcion == 3):
        codigoProducto = input("Ingrese el código del producto a buscar: ")

        for producto in productos:
            if(producto['codigo'] == codigoProducto):
                actualizarPrecio = input(f'Digite el nuevo precio del código {codigoProducto}: ')

                for i in producto:
                    producto['precio'] = actualizarPrecio

                print(producto)

            else:
                print("Digite un código válido")
                print("")

    elif(opcion == 4):
        codigoProducto = input("Ingrese el código del producto a buscar: ")

        for producto in productos:
            if(producto['codigo'] == codigoProducto):
                
                productos.remove(producto)
                print("Producto eliminado correctamente")

            else:
                print("Digite un código válido")
                print("")
    
    elif(opcion == 0):
        print("Ha decidido terminar, gracias")
        break

    else:
        print("Seleccione una opción válida")
        break
else:
    print("Hasta luego")