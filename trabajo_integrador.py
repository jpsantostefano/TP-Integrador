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
        resultado = valor1 and valor2
        print(f"La salida de {valor1} y {valor2} es: {int(resultado)}")

    elif opcion == 2:
        resultado = valor1 or valor2
        print(f"La salida de {valor1} y {valor2} es: {int(resultado)}")
elif opcion == 3:
    valor = int(input("Ingrese un valor: "))
    resultado = not valor
    print(f"La salida de NOT {valor} es: {int(resultado)}")












