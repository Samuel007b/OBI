# OBI 2022 - Fase 2 - Níveis 1 e 2
# Questão: Câmeras

N, M, K = map(int, input().split())
sala = [[0]*N for _ in range(M)]
cameras = []
for i in range(K):
    line = input()
    cameras.append([int(line[0]), int(line[2]), line[4]])
for i in range(K):
    if cameras[i][2]=='N':
        for j in range(cameras[i][1]-1, -1, -1):
            sala[j][cameras[i][0]-1] = 1
    elif cameras[i][2]=='S':
        for j in range(cameras[i][1]-1, M, 1):
            sala[j][cameras[i][0]-1] = 1
    elif cameras[i][2]=='L':
        for j in range(cameras[i][0]-1, N, 1):
            sala[cameras[i][1]-1][j] = 1
    elif cameras[i][2]=='O':
        for j in range(cameras[i][0]-1, -1, -1):
            sala[cameras[i][1]-1][j] = 1
if sala[0][0]==1 or sala[M-1][N-1]==1:
    print('N')
else:
    sala[0][0]='*'
    vigia = 1
    mapa = vigia
    while True:
        for i in range(M):
            for j in range(N):
                if sala[i][j]=='*':
                    if i-1>=0 and sala[i-1][j]==0:
                        sala[i-1][j]='*'
                        mapa+=1
                    if i+1<M and sala[i+1][j]==0:
                        sala[i+1][j]='*'
                        mapa+=1
                    if j-1>=0 and sala[i][j-1]==0:
                        sala[i][j-1]='*'
                        mapa+=1
                    if j+1<N and sala[i][j+1]==0:
                        sala[i][j+1]='*'
                        mapa+=1
                if sala[M-1][N-1]=='*':
                    break
            if sala[M-1][N-1]=='*':
                break
        if sala[M-1][N-1]=='*':
            print('S')
            break
        elif mapa==vigia:
            print('N')
            break
        else:
            vigia=mapa