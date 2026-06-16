# OBI 2026 - Fase 1 - Níveis 1 e 2
# Questão: Mercadinho

N = int(input())
fila = list(map(int, input().split()))
segundos = [0]
for i in range(N-1, -1, -1):
    segundo = 0
    if(fila[i]>=60):
        for j in range(i-1, -1, -1):
            if(fila[j]<60):
                segundo += 1
        segundos.append(segundo)
        break
print(max(segundos))