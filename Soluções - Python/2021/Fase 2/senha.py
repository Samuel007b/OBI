# OBI 2021 - Fase 2 - Níveis 2 e Sênior (Turno B)
# Questão: Senha da Vó Zinha

N, M, K = map(int, input().split())
senhaF = input()
senha = []
for i in range(len(senhaF)):
    senha.append(senhaF[i])
palavras = []
for i in range(M):
    palavras = list(map(int, input().split()))
P = int(input())

# a fazer