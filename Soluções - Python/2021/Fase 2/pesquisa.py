# OBI 2021 - Fase 2 - Nível Júnior (Turno B)
# Questão: Pesquisa de Preços

N = int(input())
estados = []
alcool = []
gasolina = []
for i in range(N):
    linha = input()
    estados.append(linha[0]+linha[1])
    A = []
    G = []
    for j in range(3, len(linha), 1):
        A.append(linha[j])
        if linha[j+1]==' ':
            Al = "".join(A)
            for k in range(j+2, len(linha), 1):
                G.append(linha[k])
            Ga = "".join(G)
            break
    alcool.append(float(Al))
    gasolina.append(float(Ga))
vantagem = []
for i in range(N):
    if gasolina[i]*0.7>=alcool[i]:
        vantagem.append(estados[i])
if len(vantagem)>0:
    for i in range(len(vantagem)):
        print(vantagem[i])
else:
    print('*')