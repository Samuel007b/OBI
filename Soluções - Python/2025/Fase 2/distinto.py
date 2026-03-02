P = int(input())
partidas = []
for i in range(P):
    L = int(input())
    A = int(input())
    B = int(input())
    jogadas = []
    bolinhas = 0
    rodadas = 0
    for j in range(A, B+1, 1):
        jogadas.append(j)
    while True:
        rodadas+=1
        bolinhas+=min(jogadas)
        jogadas.pop(jogadas.index(min(jogadas)))
        if bolinhas>=L or len(jogadas)==0:
            partidas.append(rodadas)
            break
for rod in partidas:
    print(rod)