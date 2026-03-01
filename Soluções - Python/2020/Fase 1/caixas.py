caixas = []
viagem = 3
for i in range(3):
    caixas.append(int(input()))
if caixas[0]<caixas[1] and caixas[1]<caixas[2]:
    viagem=1
elif caixas[0]<caixas[1] and caixas[1]==caixas[2]:
    viagem=2
elif caixas[0]==caixas[1] and caixas[1]==caixas[2]:
    viagem=3
elif caixas[0]==caixas[1] and caixas[1]<caixas[2]:
    if caixas[0]+caixas[1]<caixas[2]:
        viagem=1
    else:
        viagem=2
print(viagem)