# OBI 2025 - Fase 1 - Níveis Júnior e 2
# Questão: Dieta

N, M = map(int, input().split())
quantCal = 0
for i in range(N):
    P, G, C = map(int, input().split())
    quantCal += 4*P + 9*G + 4*C
print(M-quantCal)