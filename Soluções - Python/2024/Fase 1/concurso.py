# OBI 2024 - Fase 1 - Níveis Júnior, 1, 2 e Sênior
# Questão: Concurso

N, K = map(int, input().split())
nota = list(map(int, input().split()))
nota.sort()
print(nota[N-K])