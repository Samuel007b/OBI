# OBI 2024 - Fase 2 - Nível 2 (Turno B)
# Questão: Trio de Palitinhos

N = int(input())
palitos = list(map(int, input().split()))
trios = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i!=j and j!=k and i!=k:
                if palitos[i]+palitos[j]>palitos[k] and palitos[i]+palitos[k]>palitos[j] and palitos[j]+palitos[k]>palitos[i]:
                    trios+=1
print(int(trios/6))