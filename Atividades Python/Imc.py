def calcular_imc():
    
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))

        if altura <= 0:
            print("Altura inválida.")
            return

        imc = peso / (altura ** 2)
        print(f"Seu IMC é: {imc}")

        if imc < 18.5:
            print("Você está abaixo do peso.")
        elif 18.5 <= imc < 25:
            print("Seu peso está normal (saudável).")
        elif 25 <= imc < 30:
            print("Você está com sobrepeso.")
        else:
            print("Você está com obesidade.")

    except ValueError:
        print("Entrada inválida. Por favor, digite números para peso e altura.")


calcular_imc()