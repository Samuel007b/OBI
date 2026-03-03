# OBI 2023 - Fase 1 - Níveis 1 e Sênior
# Questão: Subsequência

A, B = map(int, input().split())
Sa = list(map(int, input().split()))
Sb = list(map(int, input().split()))
b = 0
for a in range(A):
    if Sa[a] == Sb[b]:
        b+=1
if b==B:
    print('S')
else:
    print('N')