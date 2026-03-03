# OBI 2020 - Fase 1 - Níveis 1, 2 e Sênior (Turno A)
# Questão: Fissura Perigosa

N, F = map(int, input().split())
matriz = []
for i in range(N):
    line = input()
    linha = []
    for j in range(N):
        linha.append(int(line[j]))
    matriz.append(linha)
if F>=matriz[0][0]:
    matriz[0][0]='*'
    avancoA = 1
    avancoB = 1
    while True:
        for i in range(N):
            for j in range(N):
                if matriz[i][j] == '*':
                    if i+1<N and matriz[i+1][j]!='*' and matriz[i+1][j]<=F:
                        matriz[i+1][j] = '*'
                        avancoB+=1
                    if i-1>=0 and matriz[i-1][j]!='*' and matriz[i-1][j]<=F:
                        matriz[i-1][j] = '*'
                        avancoB+=1
                    if j+1<N and matriz[i][j+1]!='*' and matriz[i][j+1]<=F:
                        matriz[i][j+1] = '*'
                        avancoB+=1
                    if j-1>=0 and matriz[i][j-1]!='*' and matriz[i][j-1]<=F:
                        matriz[i][j-1] = '*'
                        avancoB+=1
        if avancoB>avancoA:
            avancoA=avancoB
        else:
            break
for i in range(N):
    for j in range(N):
        print(matriz[i][j], end='')
    print()