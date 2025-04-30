def eh_palindromo(texto):

    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


palavra1 = "radar"
palavra2 = "O ceara ganhou hoje"
palavra3 = "python"

print(f"'{palavra1}' é um palíndromo? {eh_palindromo(palavra1)}")
print(f"'{palavra2}' é um palíndromo? {eh_palindromo(palavra2)}")
print(f"'{palavra3}' é um palíndromo? {eh_palindromo(palavra3)}")