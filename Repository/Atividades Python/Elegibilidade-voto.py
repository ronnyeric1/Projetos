def verificar_elegibilidade_voto():
    
    try:
        idade = int(input("Digite sua idade: "))
        if idade >= 16:
            print("Você é elegível para votar.")
        else:
            print("Você ainda não é elegível para votar.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para a idade.")


verificar_elegibilidade_voto()