# OBI 2020 - Fase 2 - Níveis 1, 2 e Sênior
# Questão: Dona Formiga

S, T, P = map(int, input().split())
alturas = list(map(int, input().split()))
tuneis = []
for i in range(T):
    tuneis.append(list(map(int, input().split())))
saloes = []
for i in range(T):
    if tuneis[i][0]==P:
        if alturas[tuneis[i][1]-1]<=alturas[P-1]:
            saloes.append(tuneis[i][1])
    elif tuneis[i][1]==P:
        if alturas[tuneis[i][0]-1]<=alturas[P-1]:
            saloes.append(tuneis[i][0])
if len(saloes)>0:
    while True:
        salas = len(saloes)
        for a in range(salas):
            for i in range(T):
                if tuneis[i][0]==saloes[a]:
                    if alturas[tuneis[i][1]-1]<=alturas[saloes[a]-1] and tuneis[i][1] not in saloes:
                        saloes.append(tuneis[i][1])
                elif tuneis[i][1]==saloes[a]:
                    if alturas[tuneis[i][0]-1]<=alturas[saloes[a]-1] and tuneis[i][0] not in saloes:
                        saloes.append(tuneis[i][0])
        if len(saloes)==salas:
            break
print(len(saloes))