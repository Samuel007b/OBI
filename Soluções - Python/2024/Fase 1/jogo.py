# OBI 2024 - Fase 1 - Níveis 2 e Sênior
# Questão: Jogo da Vida

def verificaCelula(i, j):
    vizVivas = 0
    if i-1>=0 and matrizA[i-1][j]==1:
        vizVivas+=1
    if i-1>=0 and j-1>=0 and matrizA[i-1][j-1]==1:
        vizVivas+=1
    if i-1>=0 and j+1<N and matrizA[i-1][j+1]==1:
        vizVivas+=1
    if j-1>=0 and matrizA[i][j-1]==1:
        vizVivas+=1
    if j+1<N and matrizA[i][j+1]==1:
        vizVivas+=1
    if i+1<N and matrizA[i+1][j]==1:
        vizVivas+=1
    if i+1<N and j-1>=0 and matrizA[i+1][j-1]==1:
        vizVivas+=1
    if i+1<N and j+1<N and matrizA[i+1][j+1]==1:
        vizVivas+=1
    if matrizA[i][j]==0:
        if vizVivas==3:
            matrizB[i][j]=1
        else:
            matrizB[i][j]=0
    else:
        if vizVivas<2 or vizVivas>3:
            matrizB[i][j]=0
        else:
            matrizB[i][j]=1

def showMatriz():
    for i in range(N):
        for j in range(N):
            print(matrizA[i][j], end='')
        print()

N, Q = map(int, input().split())
matrizA = []
for i in range(N):
    line = input()
    linha = []
    for j in range(N):
        linha.append(int(line[j]))
    matrizA.append(linha)
for a in range(Q):
    matrizB = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            verificaCelula(i, j)
    matrizA = matrizB
showMatriz()