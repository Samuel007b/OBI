# OBI 2020 - Fase 2 - Níveis 2 e Sênior
# Questão: Fotografia

A, L = map(int, input().split())
N = int(input())
molduras = []
for i in range(N):
    X, Y = map(int, input().split())
    area = X*Y
    molduras.append([X, Y, area])
opcoes = []
for i in range(N):
    if molduras[i][0]>=A and molduras[i][1]>=L:
        opcoes.append(i)
    elif molduras[i][1]>=A and molduras[i][0]>=L:
        opcoes.append(i)
if len(opcoes)==0:
    print('-1')
else:
    melhor = molduras[opcoes[0]][2]
    for i in range(len(opcoes)):
        if molduras[opcoes[i]][2]<melhor:
            melhor = molduras[opcoes[i]][2]
    for i in range(len(opcoes)):
        if melhor==molduras[opcoes[i]][2]:
            print(opcoes[i]+1)
            break