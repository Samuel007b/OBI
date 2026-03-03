# OBI 2020 - Fase 1 - Níveis Júnior, 2 e Sênior (Turno B)
# Questão: Camisetas da Olimpíada

N = int(input())
camisas = list(map(int, input().split()))
p = 0
m = 0
for i in range(N):
    if camisas[i]==1:
        p+=1
    elif camisas[i]==2:
        m+=1
P = int(input())
M = int(input())
if p==P and m==M:
    print('S')
else:
    print('N')