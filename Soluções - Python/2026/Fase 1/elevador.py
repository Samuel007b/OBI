# OBI 2026 - Fase 1 - Níveis Júnior e Sênior
# Questão: Elevador

N = int(input())
andares = list(map(int, input().split()))
tempo = 0
for i in range(1, len(andares)):
    tempo += abs(andares[i]-andares[i-1])
print(tempo)