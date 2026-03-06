# OBI 2020 - Fase 2 - Nível Sênior
# Questão: Caixeiro Viajante

N = int(input())
voos = []
for i in range(int(N*(N-1)/2)):
    voos.append(list(map(int, input().split())))
tempoViagem = []
viagens = []
for i in range(1, N+1, 1):
    tempo = 0
    viagem = [i]
    for j in range(i, 1, -1):
        for k in range(int(N*(N-1)/2)):
            if voos[k][0]==j and voos[k][1]==j-1:
                tempo += voos[k][2]
                viagem.append(voos[k][1])
                break
            elif voos[k][1]==j and voos[k][0]==j-1:
                tempo += voos[k][2]
                viagem.append(voos[k][0])
                break
    for k in range(int(N*(N-1)/2)):
        if voos[k][0]==1 and voos[k][1]==i+1:
            tempo += voos[k][2]
            viagem.append(voos[k][1])
            break
        elif voos[k][1]==1 and voos[k][0]==i+1:
            tempo += voos[k][2]
            viagem.append(voos[k][0])
            break
    for j in range(i+1, N, 1):
        for k in range(int(N*(N-1)/2)):
            if voos[k][0]==j and voos[k][1]==j+1:
                tempo += voos[k][2]
                viagem.append(voos[k][1])
                break
            elif voos[k][1]==j and voos[k][0]==j+1:
                tempo += voos[k][2]
                viagem.append(voos[k][0])
                break
    tempoViagem.append(tempo)
    viagens.append(viagem)
print(viagens)
print(tempoViagem)

# corrigir