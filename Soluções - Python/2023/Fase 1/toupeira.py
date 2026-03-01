S = int(input())
T = int(input())
tunel = []
for i in range(T):
    par = []
    par.append(int(input()))
    par.append(int(input()))
    tunel.append(par)
P = int(input())
passeio = []
for i in range(P):
    N = int(input())
    caminho = []
    for j in range(N):
        caminho.append(int(input()))
    passeio.append(caminho)
sugestoes = 0
for i in range(P):
    erro = False
    for j in range(len(passeio[i])-1):
        for k in range(T):
            if passeio[i][j]==tunel[k][0]:
                if passeio[i][j+1]==tunel[k][1]:
                    break
            elif passeio[i][j]==tunel[k][1]:
                if passeio[i][j+1]==tunel[k][0]:
                    break
            elif k==T-1:
                erro = True
                break
        if erro == True:
            break
    if erro == False:
        sugestoes += 1
print(sugestoes)