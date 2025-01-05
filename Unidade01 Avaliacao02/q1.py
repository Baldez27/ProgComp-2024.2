# Questão 1: Contar números decrescentes de 10 a 987631
# Alunos: Daniel Baldez - Matrícula: 20242014050023
# Github: Baldez27

# Contador para armazenar a quantidade de números decrescentes
contador_decrescentes = 0
# Começa a verificção a partir do número 10
numero = 10

# Loop através de todos os números até 987631
while numero <= 987631:
    eh_decrescente = True
    atual = numero

    # Verifica os dígitos do número
    while atual >= 10:
        ultimo_digito = atual % 10
        atual //= 10
        penultimo_digito = atual % 10
        if penultimo_digito < ultimo_digito:
            eh_decrescente = False
            break

    # Incrementa o contador se o número for decrescente
    if eh_decrescente:
        contador_decrescentes += 1
    numero += 1

# Exibe o resultado
print("Quantidade de números decrescentes:", contador_decrescentes)
