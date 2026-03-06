# OBI 2023 - Fase 2 - Níveis 2 e Sênior (Turno B)
# Questão: Fortunas

def criaReuniao(O, E, D):
    convidadas = [O]
    while True:
        num = len(convidadas)
        for i in range(N):
            if i+1 in convidadas and familia[i][1] not in convidadas:
                if familia[familia[i][1]-1][0]>=E and familia[familia[i][1]-1][0]<=D:
                    convidadas.append(familia[i][1])
            elif familia[i][1] in convidadas and i+1 not in convidadas:
                if familia[i][0]>=E and familia[i][0]<=D:
                    convidadas.append(i+1)
        if len(convidadas)==num:
            break
    return convidadas

N, M = map(int, input().split())
familia = []
convites = []
for i in range(N):
    familia.append(list(map(int, input().split())))
    convites.append(0)
reunioes = []
for i in range(M):
    reunioes.append(list(map(int, input().split())))
for i in range(M):
    convocadas = criaReuniao(reunioes[i][0], reunioes[i][1], reunioes[i][2])
    for j in range(N):
        if j+1 in convocadas:
            convites[j]+=1
for i in range(N):
    print(convites[i], end=" ")