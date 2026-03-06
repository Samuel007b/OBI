# OBI 2023 - Fase 2 - Níveis Júnior e Sênior (Turno B)
# Questão: UPA

N = int(input())
onibus = []
for i in range(N):
    onibus.append(list(map(int, input().split())))
estacionamento = []
for i in range(N):
    vagas = 1
    for j in range(N):
        if i!=j:
            if onibus[i][0]<onibus[j][0] and onibus[j][0]<onibus[i][1]:
                vagas+=1
            elif onibus[i][0]<onibus[j][1] and onibus[j][1]<onibus[i][1]:
                vagas+=1
    estacionamento.append(vagas)
print(max(estacionamento)*20)