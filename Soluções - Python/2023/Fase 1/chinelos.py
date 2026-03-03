# OBI 2023 - Fase 1 - Nível Júnior
# Questão: Chinelos

N = int(input())
estoque = []
for i in range(N):
    estoque.append(int(input()))
P = int(input())
vendas = 0
for i in range(P):
    pedido = int(input())-1
    if estoque[pedido] > 0:
        estoque[pedido] -= 1
        vendas += 1
print(vendas)