# OBI 2021 - Fase 1 - Níveis 1, 2 e Sênior
# Questão: Zero para Cancelar

N = int(input())
lista = []
for i in range(N):
    X = int(input())
    if X!=0:
        lista.append(X)
    else:
        lista.pop()
print(sum(lista))