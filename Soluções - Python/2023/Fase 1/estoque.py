# OBI 2023 - Fase 1 - Níveis 1, 2 e Sênior
# Questão: Estoque

M, N = map(int, input().split())
tipo = []
for i in range(M):
    tipo.append(list(map(int, input().split())))
P = int(input())
vendas = 0
for i in range(P):
    x, y = map(int, input().split())
    if tipo[x-1][y-1]>0:
        tipo[x-1][y-1] -= 1
        vendas += 1
print(vendas)