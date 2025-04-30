def classificar_triangulo():
    
    try:
        lado1 = float(input("Digite o comprimento do primeiro lado: "))
        lado2 = float(input("Digite o comprimento do segundo lado: "))
        lado3 = float(input("Digite o comprimento do terceiro lado: "))

        if lado1 == lado2 == lado3:
            print("O triângulo é equilátero (todos os lados iguais).")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("O triângulo é isósceles (dois lados iguais).")
        else:
            print("O triângulo é escaleno (todos os lados diferentes).")
    except ValueError:
        print("Entrada inválida. Por favor, digite números para os lados.")


classificar_triangulo()