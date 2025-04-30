def converter_temperatura(valor, unidade_entrada, unidade_saida):
   
    if unidade_entrada.upper() == "C" and unidade_saida.upper() == "F":
        return (valor * 9/5) + 32
    elif unidade_entrada.upper() == "F" and unidade_saida.upper() == "C":
        return (valor - 32) * 5/9
    else:
        return "Conversão de temperatura não suportada."

def converter_distancia(valor, unidade_entrada, unidade_saida):
    """
    Converte distância entre quilômetros e milhas.
    """
    if unidade_entrada.upper() == "KM" and unidade_saida.upper() == "MILHAS":
        return valor * 0.621371
    elif unidade_entrada.upper() == "MILHAS" and unidade_saida.upper() == "KM":
        return valor * 1.60934
    else:
        return "Conversão de distância não suportada."

temp_celsius = 25
temp_fahrenheit = converter_temperatura(temp_celsius, "C", "F")
print(f"{temp_celsius}°C é igual a {temp_fahrenheit}°F")

dist_km = 150
dist_milhas = converter_distancia(dist_km, "KM", "MILHAS")
print(f"{dist_km} km é igual a {dist_milhas} milhas")