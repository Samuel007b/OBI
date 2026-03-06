# OBI 2020 - Fase 2 - Níveis Júnior e 1
# Questão: Dona Lesma

A = int(input())
S = int(input())
D = int(input())
dias = 0
altura = 0
while True:
    dias +=1
    altura += S
    if altura>=A:
        print(dias)
        break
    else:
        altura -= D