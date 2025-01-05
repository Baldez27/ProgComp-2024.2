# Questão 5: Dias e sábados desde 27/04/1968
# Alunos: [Seu Nome] - Matrícula: 20242014050023
# Github: Baldez27

# Datas de referência
ano_inicial = 1968
mes_inicial = 4
dia_inicial = 27

# Data atual
ano_atual = 2025
mes_atual = 1
dia_atual = 5

# Contadores
dias_totais = 0
sabados_totais = 0

# Contagem de dias
ano = ano_inicial
mes = mes_inicial
dia = dia_inicial

while True:
    # Determina o número de dias no mês
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias_no_mes = 31
    elif mes in [4, 6, 9, 11]:
        dias_no_mes = 30
    elif ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        dias_no_mes = 29
    else:
        dias_no_mes = 28

    while dia <= dias_no_mes:
        dias_totais += 1
        if dias_totais % 7 == 0:
            sabados_totais += 1

        if ano == ano_atual and mes == mes_atual and dia == dia_atual:
            print("Total de dias desde 27/04/1968:", dias_totais)
            print("Total de sábados:", sabados_totais)
            exit()

        dia += 1

    # Avança para o próximo mês
    dia = 1
    mes += 1
    if mes > 12:
        mes = 1
        ano += 1
