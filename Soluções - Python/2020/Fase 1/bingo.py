# OBI 2020 - Fase 1 - Nível Sênior (Turno A)
# Questão: Bingo!

N, K, U = map(int, input().split())
bingo = []
for i in range(N):
    bingo.append(list(map(int, input().split())))
sequencia = list(map(int, input().split()))
venc = []
for i in range(U):
    for j in range(N):
        if sequencia[i] in bingo[j]:
            bingo[j].pop(bingo[j].index(sequencia[i]))
            if len(bingo[j])==0:
                venc.append(j+1)
    if len(venc)!=0:
        break
for i in venc:
    print(i, end=' ')