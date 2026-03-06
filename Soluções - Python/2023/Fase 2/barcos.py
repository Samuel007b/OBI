# OBI 2023 - Fase 2 - Níveis 2 e Sênior (Turno A)
# Questão: Barcos da Nlogônia

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

N, B = map(int, input().split())
barcos = []
for i in range(B):
    barcos.append(list(map(int, input().split())))
C = int(input())
viagens = []
for i in range(C):
    viagens.append(list(map(int, input().split())))

# a fazer