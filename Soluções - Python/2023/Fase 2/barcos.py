def encontraCaminho(X, Y):
    caminho = [X]
    ilhaA = X
    while True:
        for i in range(B):
            if barcos[i][0]==ilhaA and barcos[i][1] not in caminho:
                caminho.append(barcos[i][1])
                ilhaA=barcos[i][1]
                break
            elif barcos[i][1]==ilhaA and barcos[i][0] not in caminho:
                caminho.append(barcos[i][0])
                ilhaA=barcos[i][0]
                break
        if ilhaA==Y:
            return caminho
            break

N = int(input())
B = int(input())
barcos = []
for i in range(B):
    barco = []
    for j in range(3):
        barco.append(int(input()))
    barcos.append(barco)
C = int(input())
viagens = []
for i in range(C):
    viagem = []
    viagem.append(int(input()))
    viagem.append(int(input()))
    viagens.append(viagem)

# a fazer