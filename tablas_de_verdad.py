print("Elige que taba de verdad deseas saber: ")
print("1. AND")
print("2. OR")
print("3. NOT")
print("0. Salir")
opcion = int(input())

if opcion == 1:
    print("Tabla de verdad para AND:")
    print("A | B | Resultado")
    print("--|---|----------")
    for a in [0,1]:
        for b in [0,1]:
            resultado = a and b
            print(f"{a} | {b} |   {int(resultado)}")

elif opcion == 2:
    print("Tabla de verdad para OR:")
    print("A | B | Resultado")
    print("--|---|----------")
    for a in [0,1]:
        for b in [0,1]:
            resultado = a or b
            print(f"{a} | {b} |   {int(resultado)}")

elif opcion == 3:
    print("Tabla de verdad para NOT:")
    print("A | Resultado")
    print("--|----------")
    for a in [0,1]:
        resultado = not a
        print(f"{a} |    {int(resultado)}")

