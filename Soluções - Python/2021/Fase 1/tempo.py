# OBI 2021 - Fase 1 - Níveis 1, 2 e Sênior
# Questão: Tempo de Resposta

N = int(input())
registro = []
amigo = []
periodo = []
tempo = 0
for i in range(N):
    reg = list(map(input().split()))
    caractere = reg[0]
    num = int(reg[1])
    match caractere:
        case 'R' | 'E':
            registro.append(caractere)
            amigo.append(num)
            periodo.append(tempo)
        case 'T':
            tempo += num-1
    tempo +=1
# a fazer