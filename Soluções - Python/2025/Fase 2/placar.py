# OBI 2025 - Fase 2 - Níveis Júnior, 1 e 2
# Questão: Placar do Jogo

golsP = list(map(int, input().split()))
P = golsP[0]
golsP.pop(0)
golsC = list(map(int, input().split()))
C = golsC[0]
golsC.pop(0)
tempo = 0
Pgol = 0
Cgol = 0
print(f'{Pgol} {Cgol}')
while True:
    if Pgol+Cgol==P+C:
        break
    else:
        for i in range(P):
            if tempo==golsP[i]:
                Pgol+=1
                print(f'{Pgol} {Cgol}')
        for j in range(C):
            if tempo==golsC[j]:
                Cgol+=1
                print(f'{Pgol} {Cgol}')
        tempo+=1