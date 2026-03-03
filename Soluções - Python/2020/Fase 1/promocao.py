# OBI 2020 - Fase 1 - Nível 2 (Turno A)
# Questão: Promoção de Primeira

N = int(input())
rodovias = []
for i in range(N-1):
    rodovias.append(list(map(int, input().split())))
rotas = []
for i in range(N-1):
    cidade = [rodovias[i][0], rodovias[i][1]]
    a=i
    b=a
    while True:
        for j in range(N-1):
            if rodovias[j][2]!=rodovias[a][2] and rodovias[j][0]==rodovias[a][1] and rodovias[j][1] not in cidade:
                cidade.append(rodovias[j][1])
                b=j
                break
        if b!=a:
            a=b
        else:
            break
    rotas.append(len(cidade))
print(max(rotas))
# corrigir