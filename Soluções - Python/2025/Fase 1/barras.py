# OBI 2025 - Fase 1 - Níveis 2 e Sênior
# Questão: Gráfico de Barras

N = int(input())
brinq = list(map(int, input().split()))
for i in range(max(brinq), 0, -1):
    for j in range(N):
        if brinq[j]>=i:
            print('1', end=" ")
        else:
            print('0', end=" ")
    print()