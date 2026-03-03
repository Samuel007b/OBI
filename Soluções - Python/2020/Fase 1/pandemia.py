# OBI 2020 - Fase 1 - Níveis 1 e 2 (Turno A)
# Questão: Pandemia

N, M = map(int, input().split())
I, R = map(int, input().split())
reunioes = []
amigosInfec = [I]
for i in range(M):
    reuniao = list(map(int, input().split()))
    reuniao.pop(0)
    reunioes.append(reuniao)
for i in range(R-1, M, 1):
    for j in range(len(reunioes[i])):
        if reunioes[i][j] in amigosInfec:
            for k in range(len(reunioes[i])):
                if reunioes[i][k] not in amigosInfec:
                    amigosInfec.append(reunioes[i][k])
            break
    if len(amigosInfec)==N:
        break
print(len(amigosInfec))