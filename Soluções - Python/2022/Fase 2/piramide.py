# OBI 2022 - Fase 2 - Níveis Júnior, 1 e Sênior
# Questão: Pirâmide

N = int(input())
piramide = []
for i in range(N):
    linha = []
    for j in range(N):
        linha.append(0)
    piramide.append(linha)
nivel = 0
if N%2==0:
    for a in range(int(N/2)):
        nivel+=1
        for i in range(nivel-1, N-nivel+1, 1):
            for j in range(nivel-1, N-nivel+1, 1):
                piramide[i][j] = nivel
else:
    for a in range(int((N+1)/2)):
        nivel+=1
        for i in range(nivel-1, N-nivel+1, 1):
            for j in range(nivel-1, N-nivel+1, 1):
                piramide[i][j] = nivel
for i in range(N):
    for j in range(N):
        print(piramide[i][j], end=' ')
    print()