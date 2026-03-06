# OBI 2021 - Fase 2 - Níveis 2 e Sênior (Turno A)
# Questão: Sanduíche

N, M = map(int, input().split())
ingredientes = []
for i in range(N):
    ingredientes.append(i+1)
Ncombs = []
for i in range(M):
    Ncombs.append((map(int, input().split())))

# a fazer