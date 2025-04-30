import random

def jogo_adivinhacao():
    
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Adivinhe o número entre 1 e 10: "))
            tentativas += 1

            if palpite == numero_secreto:
                print(f"Parabéns! Você adivinhou em {tentativas} tentativas.")
                break
            elif palpite < numero_secreto:
                print("O número secreto é maior.")
            else:
                print("O número secreto é menor.")
        except ValueError:
            print("Por favor, digite um número inteiro.")


jogo_adivinhacao()