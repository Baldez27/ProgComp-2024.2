# Questão 2: Contar números palíndromos de 10 a 100000
# Alunos: Daniel Baldez - Matrícula: 20242014050023
# Github: Baldez27

# Contador para armazenar a quantidade de palíndromos
contador_palindromos = 0
# Começa a verificção a partir do número 10
numero = 10

# Loop através de todos os números até 100000
while numero <= 100000:
    invertido = 0
    original = numero
    atual = numero

    # Calcula o número invertido
    while atual > 0:
        resto = atual % 10
        invertido = invertido * 10 + resto
        atual //= 10

    # Verifica se o número é palíndromo
    if original == invertido:
        contador_palindromos += 1
    numero += 1

# Exibe o resultado
print("Quantidade de números palíndromos:", contador_palindromos)
