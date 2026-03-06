# OBI 2022 - Fase 2 - Níveis 2 e Sênior
# Questão: Viagem

V, N, M = map(int, input().split())
rotas = []
for i in range(M):
    rotas.append(list(map(int, input().split())))
X, Y = map(int, input().split())

# a fazer