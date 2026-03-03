# OBI 2024 - Fase 2 - Níveis 1 e 2
# Questão: Concatena Dígitos

N, Q = map(int, input().split())
lista = list(map(int, input().split()))
potenciais = []
for i in range(Q):
    L, R = map(int, input().split())
    potencial = 0
    for j in range(L-1, R, 1):
        potencial+=lista[j]
    potencial*=11*(R-L)
    potenciais.append(potencial)
for i in range(Q):
    print(potenciais[i])