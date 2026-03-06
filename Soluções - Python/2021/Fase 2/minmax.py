# OBI 2021 - Fase 2 - Nível Sênior (Turno B)
# Questão: Mínimo e Máximo

S = int(input())
A = int(input())
B = int(input())
numeros = []
for i in range(A, B+1, 1):
    somaAlg = sum(int(dig) for dig in str(i))
    if somaAlg == S:
        numeros.append(i)
print(f"{min(numeros)}\n{max(numeros)}")