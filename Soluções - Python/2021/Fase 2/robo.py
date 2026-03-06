# OBI 2021 - Fase 2 - Níveis Júnior e 1 (Turno A)
# Questão: Robô

N, C, S = map(int, input().split())
comandos = list(map(int, input().split()))
estacaoAtual = 1
vezes = 0
if estacaoAtual==S:
    vezes+=1
for i in range(len(comandos)):
    estacaoAtual += comandos[i]
    if estacaoAtual==0:
        estacaoAtual=N
    elif estacaoAtual==N+1:
        estacaoAtual=1
    if estacaoAtual==S:
        vezes+=1
print(vezes)