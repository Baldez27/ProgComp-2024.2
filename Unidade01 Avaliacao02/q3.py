# Questão 3: Contar pares de primos ímpares consecutivos menores que 1.000.000
# Alunos: [Seu Nome] - Matrícula: 20242014050023
# Github: Baldez27

# Contador para armazenar a quantidade de pares de primos
contador_pares = 0
# Começa a verificção a partir do número 3
numero = 3
ultimo_primo = 0

# Loop através de todos os números ímpares menores que 1.000.000
while numero < 1000000:
    eh_primo = True
    divisor = 2

    # Verifica se o número é primo
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1

    # Se for primo, verifica se forma um par consecutivo
    if eh_primo:
        if ultimo_primo != 0 and numero - ultimo_primo == 2:
            contador_pares += 1
        ultimo_primo = numero

    # Incrementa o número em 2 para continuar com ímpares
    numero += 2

# Exibe o resultado
print("Quantidade de pares de primos consecutivos:", contador_pares)
