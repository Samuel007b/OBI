N = int(input())
Q = int(input())
lista = []
for i in range(N):
    lista.append(int(input()))
potenciais = []
for i in range(Q):
    L = int(input())
    R = int(input())
    potencial = 0
    for j in range(L-1, R, 1):
        potencial+=lista[j]
    potencial*=11*(R-L)
    potenciais.append(potencial)
for i in range(Q):
    print(potenciais[i])