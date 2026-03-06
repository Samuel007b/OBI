# OBI 2021 - Fase 2 - Níveis 1, 2 e Sênior (Turno A)
# Questão: Retângulo

N = int(input())
arvores = list(map(int, input().split()))
pontos = [0]
ponto = 0
for i in range(len(arvores)):
    ponto+=arvores[i]
    pontos.append(ponto)
arco = pontos[len(pontos)-1]
pontos.pop(len(pontos)-1)
erro = True
for i in range(len(pontos)):
    for j in range(len(pontos)):
        if i!=j:
            pontoC = (pontos[i]+int(arco/2))%arco
            pontoD = (pontos[j]+int(arco/2))%arco
            if pontoC in pontos and pontoD in pontos:
                erro = False
                print('S')
                break
    if erro==False:
        break
if erro==True:
    print('N')