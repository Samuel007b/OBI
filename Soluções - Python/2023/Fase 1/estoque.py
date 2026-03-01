M = int(input())
N = int(input())
tipo = []
for i in range(M):
    tamanho = []
    for j in range(N):
        tamanho.append(int(input()))
    tipo.append(tamanho)
vendas = 0
P = int(input())
for i in range(P):
    x = int(input())-1
    y = int(input())-1
    if tipo[x][y]>0:
        tipo[x][y] -= 1
        vendas += 1
print(vendas)