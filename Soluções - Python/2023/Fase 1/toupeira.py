# OBI 2023 - Fase 1 - Níveis 2 e Sênior
# Questão: Toupeira

S, T = map(int, input().split())
tunel = []
for i in range(T):
    tunel.append(list(map(int, input().split())))
P = int(input())
passeio = []
for i in range(P):
    caminho = list(map(int, input().split()))
    caminho.pop(0)
    passeio.append(caminho)
sugestoes = 0
for i in range(P):
    erro = False
    for j in range(len(passeio[i])-1):
        for k in range(T):
            if passeio[i][j]==tunel[k][0]:
                if passeio[i][j+1]==tunel[k][1]:
                    break
            elif passeio[i][j]==tunel[k][1]:
                if passeio[i][j+1]==tunel[k][0]:
                    break
            elif k==T-1:
                erro = True
                break
        if erro == True:
            break
    if erro == False:
        sugestoes += 1
print(sugestoes)