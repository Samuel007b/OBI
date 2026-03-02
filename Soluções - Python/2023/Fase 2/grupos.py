E = int(input())
M = int(input())
D = int(input())
duplas = []
brigas = []
trios = []
for i in range(M):
    dupla = []
    dupla.append(int(input()))
    dupla.append(int(input()))
    duplas.append(dupla)
for i in range(D):
    briga = []
    briga.append(int(input()))
    briga.append(int(input()))
    brigas.append(briga)
restricoes = 0
for i in range(int(E/3)):
    A = int(input())
    B = int(input())
    C = int(input())
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