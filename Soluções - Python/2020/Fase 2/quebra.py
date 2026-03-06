# OBI 2020 - Fase 2 - Níveis 2 e Sênior
# Questão: Quebra-Cabeças

N = int(input())
fichas1 = list(map(int, input().split()))
fichas1.pop(0)
fichas2 = list(map(int, input().split()))
fichas2.pop(0)
fichas = []
for f in fichas1:
    fichas.append(f)
for f in fichas2:
    fichas.append(f)
# a fazer