# OBI 2023 - Fase 2 - Níveis Júnior, 1 e 2 (Turno B)
# Questão: Empresa

def calculaInsatisfacao():
    insatisfeitos = 0
    for a in range(N):
        for b in range(len(chefes[a])):
            if funcionarios[chefes[a][b]][1]>funcionarios[a][1]:
                insatisfeitos+=1
    return insatisfeitos

N = int(input())
funcionarios = []
for i in range(N):
    funcionarios.append(list(map(int, input().split())))
chefes = []
for i in range(N):
    subordinados = []
    for j in range(N):
        if funcionarios[j][0]==i+1:
            subordinados.append(j)
    chefes.append(subordinados)
A = int(input())
ajustes = []
for i in range(A):
    ajustes.append(list(map(int, input().split())))
print(calculaInsatisfacao())
for i in range(A):
    funcionarios[ajustes[i][0]-1][1] = ajustes[i][1]
    print(calculaInsatisfacao())