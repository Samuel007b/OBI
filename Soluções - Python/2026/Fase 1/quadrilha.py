# OBI 2026 - Fase 1 (Turno B) - Níveis Mirim, Júnior e 2
# Questão: Dança de Quadrilha

N = int(input())
t = list(map(int, input().split()))
d = 0
for i in range(len(t)):
    if(i%2==0):
        d+=t[i]
    else:
        d-=t[i]
print(abs(d))