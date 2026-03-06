# OBI 2023 - Fase 2 - Níveis 1, 2 e Sênior (Turno A)
# Questão: Intervalo Distinto

N = int(input())
sequencia = []
for i in range(N):
    sequencia.append(int(input()))
distintos = []
for i in range(N):
    elementos = [sequencia[i]]
    for j in range(i+1, N, 1):
        if sequencia[j] not in elementos:
            elementos.append(sequencia[j])
        else:
            break
    distintos.append(len(elementos))
print(max(distintos))