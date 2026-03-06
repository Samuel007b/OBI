# OBI 2021 - Fase 2 - Níveis 2 e Sênior (Turno B)
# Questão: Poligrama

def checarParte(partes):
    for a in range(1, len(partes)):
        parte0 = partes[0].copy()
        for b in range(len(partes[0])):
            if partes[a][b] in parte0:
                parte0.pop(parte0.index(partes[a][b]))
            else:
                return False
    return True

N = int(input())
P = input()
palavra = []
for i in range(len(P)):
    palavra.append(P[i])
erro = False
for i in range(len(palavra)):
    if len(palavra)%(i+1)!=0 or (i+1)>len(palavra)/2:
        break
    erro = False
    partes = []
    for j in range(int(len(palavra)/(i+1))):
        parte = []
        for k in range(j*(i+1), (j+1)*(i+1), 1):
            parte.append(palavra[k])
        partes.append(parte)
    if checarParte(partes):
        for j in range(len(partes[0])):
            print(partes[0][j], end="")
        break
    else:
        erro = True
if erro==True:
    print('*')