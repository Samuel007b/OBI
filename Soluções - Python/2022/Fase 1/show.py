# OBI 2022 - Fase 1 - Nível 1
# Questão: Show

A, N, M = map(int, input().split())
fila = []
for i in range(N):
    fila.append(list(map(int, input().split())))
sucesso = False
for i in range(N-1, -1, -1):
    assentos = 0
    for j in range(M):
        if fila[i][j]==0:
            assentos+=1
            if assentos == A:
                sucesso = True
                break
        else:
            assentos=0
    if sucesso == True:
        opcao = N-i
        break
if sucesso == False:
    opcao = -1
print(opcao)