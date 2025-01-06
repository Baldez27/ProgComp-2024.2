# Questão 4: Jogo de palavras Dueto
# Alunos: Daniel Baldez - Matrícula: 20242014050023
# Github: Baldez27

# Palavras a serem descobertas
palavra1 = "mesa"
palavra2 = "gato"

# Máximo de tentativas
max_tentativas = 7
tentativas = 0

# Início do jogo
while tentativas < max_tentativas:
    tentativas += 1
    print(f"Tentativa {tentativas}/{max_tentativas}: Digite uma palavra válida de 4 letras:")

    tentativa = input().strip().lower()

    # Verifica se a entrada é válida (4 letras)
    if len(tentativa) != 4:
        print("Entrada inválida! Digite exatamente 4 letras.")
        continue

    # Inicializa o feedback para ambas as palavras
    feedback1 = ""
    feedback2 = ""

    # Verifica as letras da tentativa em relação à palavra1
    i = 0
    while i < 4:
        if i < len(palavra1) and tentativa[i] == palavra1[i]:
            feedback1 += tentativa[i].upper()  # Letra correta na posição correta
        elif tentativa[i] in palavra1:
            feedback1 += tentativa[i]  # Letra correta em posição errada
        else:
            feedback1 += "_"  # Letra ausente
        i += 1

    # Verifica as letras da tentativa em relação à palavra2
    i = 0
    while i < 4:
        if i < len(palavra2) and tentativa[i] == palavra2[i]:
            feedback2 += tentativa[i].upper()  # Letra correta na posição correta
        elif tentativa[i] in palavra2:
            feedback2 += tentativa[i]  # Letra correta em posição errada
        else:
            feedback2 += "_"  # Letra ausente
        i += 1

    # Mostra o feedback no terminal
    print("Palavra 1:", feedback1)
    print("Palavra 2:", feedback2)

    # Verifica se todas as palavras foram descobertas
    if feedback1 == palavra1.upper() and feedback2 == palavra2.upper():
        print("Parabéns! Você descobriu as duas palavras!")
        break
else:
    print("Fim de jogo! Você não conseguiu descobrir as palavras.")
