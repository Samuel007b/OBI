# OBI 2024 - Fase 2 - Níveis 1 e Sênior
# Questão: Dança de Formatura

def fazPasso(com, n, m):
    meio = []
    if com=='L':
        for i in range(M):
            meio.append(danca[n][i])
            danca[n][i]=danca[m][i]
            danca[m][i]=meio[i]
    elif com=='C':
        for i in range(N):
            meio.append(danca[i][n])
            danca[i][n]=danca[i][m]
            danca[i][m]=meio[i]

N, M, P = map(int, input().split())
danca = []
a = 1
for i in range(N):
    linha = []
    for j in range(M):
        linha.append(a)
        a+=1
    danca.append(linha)
for i in range(P):
    passo = input()
    O = passo[0]
    A = int(passo[2])
    B = int(passo[4])
    fazPasso(O, A-1, B-1)
for i in range(N):
    for j in range(M):
        print(danca[i][j], end=" ")
    print()