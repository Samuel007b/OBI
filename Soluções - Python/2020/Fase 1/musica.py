# OBI 2020 - Fase 1 - Nível Sênior (Turno B)
# Questão: Música para Todos

N, M, C = map(int, input().split())
musicaA = []
musicaD = []
for i in range(N):
    musicas = list(map(int, input().split()))
    musicaA.append(musicas[0])
    musicaD.append(musicas[1])
# a fazer