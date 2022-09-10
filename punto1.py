# 1.Construir un programa que permita ingresar N (cantidad digitada por # el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron ingresados (+1)

""" 1.Construir un programa que permita ingresar N (cantidad digitada por
el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3
fueron ingresados  """
print("********* Multiplos de 2 y 3 **********\n")
cantidad = int(input("Digite la cantidad de números a consultar: "))

multiplos2 = []
multiplos3 = []
multiplosRepetidos = []




for i in range(cantidad):
    numero = int(input("Digite un número: "))
    
    if numero % 2 == 0 and numero % 3 == 0:
        multiplosRepetidos.append(numero)
        multiplos2.append(numero)
        multiplos3.append(numero)
        
        
    elif numero % 2 == 0:
        multiplos2.append(numero)
    elif numero % 3 == 0:
        multiplos3.append(numero)
    else:
        print("No es multiplo de 2 ni 3")


print('Total de números multiplos de 2  = ', len(multiplos2))
print('Total de números multiplos de 3  = ', len(multiplos3))
print('Multiplos de ambos  = ', len(multiplosRepetidos))



