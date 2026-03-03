# OBI 2022 - Fase 1 - Níveis 2 e Sênior
# Questão: Maior Valor

N = int(input())
M = int(input())
S = int(input())
num = -1
for i in range(M, N-1, -1):
    soma = sum(int(digito) for digito in str(i))
    if soma==S:
        num = i
        break
print(num)