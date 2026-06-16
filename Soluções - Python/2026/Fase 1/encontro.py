# OBI 2026 - Fase 1 - Níveis 1, 2 e Sênior
# Questão: Encontro de Amigas

A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())
C1 = int(input())
C2 = int(input())
dias = 0
for i in range(31):
    if (i+1 >= A1 and i+1<=A2):
        if (i+1 >= B1 and i+1<=B2):
            if (i+1 >= C1 and i+1<=C2):
                dias += 1
print(dias)