N = int(input())
linha = []
somas = []
for i in range(N):
    coluna = []
    for j in range(N):
        coluna.append(int(input()))
    linha.append(coluna)
    somas.append(sum(coluna))
for i in range(N):
    for j in range(N):
        if linha[i][j] == 0:
            x = i+1
            y = j+1
somas.sort()
num = somas[N-1] - somas[0]
print(f'{num}\n{x}\n{y}')