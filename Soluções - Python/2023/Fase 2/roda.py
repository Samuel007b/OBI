# OBI 2023 - Fase 2 - Níveis Júnior, 1, 2 e Sênior (Turno B)
# Questão: Brincadeira de Roda

N = int(input())
I = int(input())
P = int(input())
P %= N
for i in range(P):
    I+=1
    if I==N+1:
        I=1
print(I)