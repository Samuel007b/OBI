# OBI 2026 - Fase 1 - Níveis 2 e Sênior
# Questão: Torre de Números

N = int(input())
torre = [N]
while True:
    algarismos = [int(torre[len(torre)-1]/1000), int((torre[len(torre)-1]%1000)/100), int((torre[len(torre)-1]%100)/10), torre[len(torre)-1]%10]
    algarismos.sort()
    X = (algarismos[3]*1000 + algarismos[2]*100 + algarismos[1]*10 + algarismos[0]) - (algarismos[3] + algarismos[2]*10 + algarismos[1]*100 + algarismos[0]*1000)
    if(X in torre):
        break
    else:
        torre.append(X)
for i in range(len(torre)):
    print(torre[i])