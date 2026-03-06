# OBI 2021 - Fase 2 - Níveis 1 e 2 (Turno B)
# Questão: Cálculo Rápido

S = int(input())
A = int(input())
B = int(input())
numeros = 0
for i in range(A, B+1, 1):
    somaAlg = sum(int(dig) for dig in str(i))
    if somaAlg == S:
        numeros+=1
print(numeros)