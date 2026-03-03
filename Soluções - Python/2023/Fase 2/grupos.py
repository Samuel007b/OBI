# OBI 2023 - Fase 2 - Níveis Júnior, 1, 2 e Sênior
# Questão: Grupos de Trabalho

E, M, D = map(int, input().split())
duplas = []
brigas = []
trios = []
for i in range(M):
    duplas.append(list(map(int, input().split())))
for i in range(D):
    brigas.append(list(map(int, input().split())))
restricoes = 0
for i in range(int(E/3)):
    A, B, C = map(int, input().split())
    for i in range(M):
        if A==duplas[i][0]:
            if B!=duplas[i][1] and C!=duplas[i][1]:
                restricoes+=1
        elif A==duplas[i][1]:
            if B!=duplas[i][0] and C!=duplas[i][0]:
                restricoes+=1
        if B==duplas[i][0]:
            if A!=duplas[i][1] and C!=duplas[i][1]:
                restricoes+=1
        elif B==duplas[i][1]:
            if A!=duplas[i][0] and C!=duplas[i][0]:
                restricoes+=1
        if C==duplas[i][0]:
            if A!=duplas[i][1] and B!=duplas[i][1]:
                restricoes+=1
        elif C==duplas[i][1]:
            if A!=duplas[i][0] and B!=duplas[i][0]:
                restricoes+=1
    for i in range(D):
        if A==brigas[i][0]:
            if B==brigas[i][1] or C==brigas[i][1]:
                restricoes+=1
        elif A==brigas[i][1]:
            if B==brigas[i][0] or C==brigas[i][0]:
                restricoes+=1
        if B==brigas[i][0]:
            if A==brigas[i][1] or C==brigas[i][1]:
                restricoes+=1
        elif B==brigas[i][1]:
            if A==brigas[i][0] or C==brigas[i][0]:
                restricoes+=1
        if C==brigas[i][0]:
            if A==brigas[i][1] or B==brigas[i][1]:
                restricoes+=1
        elif C==brigas[i][1]:
            if A==brigas[i][0] or B==brigas[i][0]:
                restricoes+=1
print(int(restricoes/2))