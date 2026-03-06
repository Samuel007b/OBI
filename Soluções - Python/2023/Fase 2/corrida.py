# OBI 2023 - Fase 2 - Níveis 1, 2 e Sênior (Turno B)
# Questão: Corrida de Rua

N = int(input())
trechos = []
for i in range(N):
    line = input()
    trechos.append([int(line[0]), line[2]])
pontosH = [0]
pontosV = [0]
pontoAtual = [0, 0]
for i in range(N):
    if trechos[i][1] == 'N':
        pontoAtual[1]+=trechos[i][0]
    if trechos[i][1] == 'S':
        pontoAtual[1]-=trechos[i][0]
    if trechos[i][1] == 'L':
        pontoAtual[0]+=trechos[i][0]
    if trechos[i][1] == 'O':
        pontoAtual[0]-=trechos[i][0]
    pontosH.append(pontoAtual[0])
    pontosV.append(pontoAtual[1])
print(2*(max(pontosH)-min(pontosH)+2)+2*(max(pontosV)-min(pontosV)+2))