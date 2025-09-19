print("Conversor de numeros")
print("1. Convertir decimal a binario")
print("2. Convertir binario a decimal")
print("3. Salir")

opcion = int(input("Elige una opcion: "))

if opcion == 1:
    decimal = int(input("Ingrese un numero decimal: "))
    binario = bin(decimal)[2:]
    print(f"{decimal} en binario es: {binario}")
elif opcion == 2:
    binario = input("Ingrese un numero binario: ")
    decimal = int(binario, 2)
    print(f"{binario} en decimal es: {decimal}")





