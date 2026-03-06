# OBI 2021 - Fase 2 - Níveis Júnior e 1 (Turno B)
# Questão: Potência

N = int(input())
potencias = []
for i in range(N):
    num = int(input())
    potencias.append(int(pow((num-num%10)/10, num%10)))
print(sum(potencias))