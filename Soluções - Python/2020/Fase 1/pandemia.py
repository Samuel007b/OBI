N = int(input())
M = int(input())
I = int(input())-1
R = int(input())-1
reunioes = []
amigosInfec = [I]
for i in range(M):
    reuniao = []
    A = int(input())
    for j in range(A):
        reuniao.append(int(input())-1)
    reunioes.append(reuniao)
for i in range(R, M, 1):
    for j in range(len(reunioes[i])):
        if reunioes[i][j] in amigosInfec:
            for k in range(len(reunioes[i])):
                if reunioes[i][k] not in amigosInfec:
                    amigosInfec.append(reunioes[i][k])
            break
print(len(amigosInfec))