N = int(input())
M = int(input())
bandeja = []
bandejaP = [[0]*M for _ in range(N)]
bandejaI = [[0]*M for _ in range(N)]
impar = 0
par = 0
for i in range(N):
    linha = []
    for j in range(M):
        G = int(input())
        if G%2==0:
            par+=1
        else:
            impar+=1
        linha.append(G)
    bandeja.append(linha)
gotasP = 0
gotasI = 0
for i in range(N):
    for j in range(M):
        if (i+j)%2==0:
            if bandeja[i][j]%2==1:
                bandejaP[i][j] = bandeja[i][j]+1
                gotasP+=1
            else:
                bandejaP[i][j] = bandeja[i][j]
        else:
            if bandeja[i][j]%2==0:
                bandejaP[i][j] = bandeja[i][j]+1
                gotasP+=1
            else:
                bandejaP[i][j] = bandeja[i][j]
for i in range(N):
    for j in range(M):
        if (i+j)%2==0:
            if bandeja[i][j]%2==0:
                bandejaI[i][j] = bandeja[i][j]+1
                gotasI+=1
            else:
                bandejaI[i][j] = bandeja[i][j]
        else:
            if bandeja[i][j]%2==1:
                bandejaI[i][j] = bandeja[i][j]+1
                gotasI+=1
            else:
                bandejaI[i][j] = bandeja[i][j]
if gotasP<gotasI:
    print(gotasP)
    for i in range(N):
        for j in range(M):
            print(bandejaP[i][j], end=" ")
        print()
else:
    print(gotasI)
    for i in range(N):
        for j in range(M):
            print(bandejaI[i][j], end=" ")
        print()