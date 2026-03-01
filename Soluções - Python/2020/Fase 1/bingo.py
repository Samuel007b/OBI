N = int(input())
K = int(input())
U = int(input())
bingo = []
for i in range(N):
    cartela = []
    for j in range(K):
        cartela.append(int(input()))
    bingo.append(cartela)
sequencia = []
for i in range(U):
    sequencia.append(int(input()))
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