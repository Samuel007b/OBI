# OBI 2020 - Fase 2 - Nível Júnior
# Questão: Palavras Cruzadas

Ph = input()
Pv = input()
palavraH = []
for i in range(len(Ph)):
    palavraH.append(Ph[i])
palavraV = []
for i in range(len(Pv)):
    palavraV.append(Pv[i])
encontros = []
for i in range(len(palavraV)):
    if palavraV[i] in palavraH:
        encontro = []
        for j in range(len(palavraH)-1, -1, -1):
            if palavraH[j]==palavraV[i]:
                encontro.append(j+1)
                break
        encontro.append(i+1)
        encontros.append(encontro)
if len(encontros)==0:
    print('-1 -1')
else:
    maxH = encontros[0][0]
    maxV = encontros[0][1]
    for i in range(len(encontros)):
        if encontros[i][0]>maxH:
            maxH = encontros[i][0]
            maxV = encontros[i][1]
        elif encontros[i][0]==maxH:
            if encontros[i][1]>maxV:
                maxV = encontros[i][1]
    print(f"{maxH} {maxV}")