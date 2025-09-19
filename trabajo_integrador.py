# Simulacion de Puertas Logicas Basicas:

print("PROYECTO MATEMATICA Y PROGRAMACION")

print("Elige que puerta logica deseas usar: ")
print("1. AND")
print("2. OR")
print("3. NOT")
print("0. Salir")
opcion = int(input())

if opcion == 1 or opcion == 2:
    valor1 = int(input("Ingrese el primer valor (0-1): "))
    valor2 = int(input("Ingrese el segundo valor (0-1): "))
    if opcion == 1:
        if valor1 == 1 and valor2 == 1:
            print(f"La salida de {valor1} y {valor2} es: 1")
        else:
            print(f"La salida de {valor1} y {valor2} es: 0")
    elif opcion == 2:
        if valor1 == 0 and valor2 == 0:
            print(f"La salida de {valor1} o {valor2} es: 0")
        else:
            print(f"La salida de {valor1} o {valor2} es: 1")
    else:
        valor = int(input("Ingrese un valor: "))
        if valor == 0:
            print(f"La salida de {valor} es 1")
        else:
            print(f"La salida de {valor} es 0")











