while True:
    print("MENU PRINCIPAL")
    print("1. Simulador de puertas logicas")
    print("2. Tabla de verdad")
    print("3. Conversor de Numeros")
    print("0. Salir")

    menu_opcion = int(input("Elige una opcion: "))

    if menu_opcion == 1:
        # SIMULACION DE PUERTAS LOGICAS BASICAS:
        while True:
            print("Elige que puerta logica deseas usar: ")
            print("1. AND")
            print("2. OR")
            print("3. NOT")
            print("0. Menu Principal")
            opcion1 = int(input("Elige una opcion: "))

            if opcion1 == 1 or opcion1 == 2:
                valor1 = int(input("Ingrese el primer valor (0-1): "))
                valor2 = int(input("Ingrese el segundo valor (0-1): "))
                if opcion1 == 1:
                    resultado = valor1 and valor2
                    print(f"La salida de {valor1} y {valor2} es: {int(resultado)}")

                elif opcion1 == 2:
                    resultado = valor1 or valor2
                    print(f"La salida de {valor1} y {valor2} es: {int(resultado)}")

                elif opcion1 == 3:
                    valor = int(input("Ingrese un valor: "))
                    resultado = not valor
                    print(f"La salida de NOT {valor} es: {int(resultado)}")
                
            elif opcion1 == 0:
                print("")
                break

            else:
                print("Opcion invalida")

    if menu_opcion == 2:
        # TABLAS DE VERDAD
        while True:
            print("Elige que taba de verdad deseas saber: ")
            print("1. AND")
            print("2. OR")
            print("3. NOT")
            print("0. Menu Principal")
            opcion2 = int(input("Elige una opcion: "))

            if opcion2 == 1:
                print("Tabla de verdad para AND:")
                print("A | B | Resultado")
                print("--|---|----------")
                for a in [0,1]:
                    for b in [0,1]:
                        resultado = a and b
                        print(f"{a} | {b} |   {int(resultado)}")

            elif opcion2 == 2:
                print("Tabla de verdad para OR:")
                print("A | B | Resultado")
                print("--|---|----------")
                for a in [0,1]:
                    for b in [0,1]:
                        resultado = a or b
                        print(f"{a} | {b} |   {int(resultado)}")

            elif opcion2 == 3:
                print("Tabla de verdad para NOT:")
                print("A | Resultado")
                print("--|----------")
                for a in [0,1]:
                    resultado = not a
                    print(f"{a} |    {int(resultado)}")

            elif opcion2 == 0:
                print("")
                break

            else:
                print("Opcion invalida")

    if menu_opcion == 3:
    # CONVERTIR DECIMAL A BINARIO Y VICEVERSA
        while True:
            print("Conversor")
            print("1. Convertir decimal a binario")
            print("2. Convertir binario a decimal")
            print("0. Menu Principal")

            opcion3 = int(input("Elige una opcion: "))

            if opcion3 == 1:
                decimal = int(input("Ingrese un numero decimal: "))
                binario = bin(decimal)[2:]
                print(f"{decimal} en binario es: {binario}")

            elif opcion3 == 2:
                binario = input("Ingrese un numero binario: ")
                decimal = int(binario, 2)
                print(f"{binario} en decimal es: {decimal}")

            elif opcion3 == 0:
                print("")
                break

            else:
                print("Opcion invalida")
        
    elif menu_opcion == 0:
        break

    else:
        print("Opcion invalida")




