def sistema_notas():
    
    try:
        nota = float(input("Digite a nota do aluno (0-10): "))
        if 9.0 <= nota <= 10.0:
            conceito = "A"
        elif 7.0 <= nota < 9.0:
            conceito = "B"
        elif 5.0 <= nota < 7.0:
            conceito = "C"
        elif 3.0 <= nota < 5.0:
            conceito = "D"
        elif 0.0 <= nota < 3.0:
            conceito = "F"
        else:
            conceito = "Nota inválida."
            conceito = None

        if conceito:
            print(f"A nota {nota} corresponde ao conceito: {conceito}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número para a nota.")


sistema_notas()