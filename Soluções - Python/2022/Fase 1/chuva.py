# OBI 2022 - Fase 1 - Níveis 2 e Sênior
# Questão: Chuva

N = int(input())
S = int(input())
chuvas = list(map(int, input().split()))
intervalos = 0
for i in range(N):
    quant = chuvas[i]
    if i!=N-1:
        for j in range(i+1, N, 1):
            if quant<S:
                quant += chuvas[j]
            elif quant==S and chuvas[j]==0:
                intervalos += 1
            else:
                break
    if quant==S:
        intervalos += 1
print(intervalos)