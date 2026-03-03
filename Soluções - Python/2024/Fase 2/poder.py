# OBI 2024 - Fase 2 - Níveis 2 e Sênior
# Questão: Jogo do Poder

def calculaPoder(a, b):
    copia = []
    for i in range(N):
        linha = []
        for j in range(M):
            linha.append(matriz[i][j])
        copia.append(linha)
    poder = copia[a][b]
    copia[a][b] = '*'
    while True:
        forca = poder
        for i in range(N):
            for j in range(M):
                if copia[i][j]=='*':
                    if i+1<N and copia[i+1][j]!='*' and copia[i+1][j]<=poder:
                        poder+=copia[i+1][j]
                        copia[i+1][j] = '*'
                    if i-1>=0 and copia[i-1][j]!='*' and copia[i-1][j]<=poder:
                        poder+=copia[i-1][j]
                        copia[i-1][j] = '*'
                    if j+1<M and copia[i][j+1]!='*' and copia[i][j+1]<=poder:
                        poder+=copia[i][j+1]
                        copia[i][j+1] = '*'
                    if j-1>=0 and copia[i][j-1]!='*' and copia[i][j-1]<=poder:
                        poder+=copia[i][j-1]
                        copia[i][j-1] = '*'
        if poder==forca:
            return poder
            break

N, M = map(int, input().split())
matriz = []
for i in range(N):
    matriz.append(list(map(int, input().split())))
poderF = []
for i in range(N):
    linha = []
    for j in range(M):
        linha.append(calculaPoder(i, j))
    poderF.append(linha)
for i in range(N):
    for j in range(M):
        print(poderF[i][j], end=" ")
    print()