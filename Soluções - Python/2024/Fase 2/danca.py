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

N = int(input())
M = int(input())
danca = []
a = 1
for i in range(N):
    linha = []
    for j in range(M):
        linha.append(a)
        a+=1
    danca.append(linha)
P = int(input())
for i in range(P):
    O = input()
    A = int(input())
    B = int(input())
    fazPasso(O, A-1, B-1)
for i in range(N):
    for j in range(M):
        print(danca[i][j], end=" ")
    print()