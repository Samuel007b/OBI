A = int(input())
N = int(input())
M = int(input())
fila = []
for i in range(N):
    fileira = []
    for j in range(M):
        fileira.append(int(input()))
    fila.append(fileira)
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