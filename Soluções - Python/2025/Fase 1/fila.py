# OBI 2025 - Fase 1 - Níveis 1 e Sênior
# Questão: Fila

N = int(input())
alunos = list(map(int, input().split()))
colas = 0
for i in range(N-1, -1, -1):
    if i!=N-1:
        i=j
    for j in range(i-1, -1, -1):
        if alunos[i]>alunos[j]:
            colas+=1
        else:
            break
    if(j==0):
        break
print(colas)