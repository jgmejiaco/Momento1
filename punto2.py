# 2. Leer el nombre de 10 frutas {nombre, color, precio} para preparar un salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al mismo tiempo en sentido inverso al ingresado+(1)

frutas = []

for i in range(3):
    fruta = {}
    fruta['nombre'] = input(f'Ingrese nombre de la fruta {i + 1} de 10: ')
    fruta['color'] = input(f'Ingrese color de la fruta {i + 1} de 10: ')
    fruta['precio'] = int(input(f'Ingrese precio de la fruta {i + 1} de 10: '))

    frutas.append(fruta)

# for llave, valor in fruta.items():
#     print(fruta)
#     print("")

print(fruta)
# print(fruta['nombre'])
print("")
print(frutas)
frutas.reverse()
print(frutas)