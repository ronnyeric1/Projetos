def calculadora_simples():
   
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Erro! Divisão por zero."
        else:
            resultado = "Operação inválida."

        print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números.")


calculadora_simples()