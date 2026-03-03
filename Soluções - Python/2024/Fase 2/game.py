# OBI 2024 - Fase 2 - Nível 2 (Turno B)
# Questão: Game Show

N = int(input())
a = input()
sala = 1
for i in range(N):
    if a[i]=='D':
        sala = 2*sala+1
    elif a[i]=='E':
        sala *= 2
print(sala)