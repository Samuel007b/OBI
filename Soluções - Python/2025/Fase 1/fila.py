N = int(input())
alunos = []
colas = 0
for i in range(N):
    alunos.append(int(input()))
for i in range(N-1, -1, -1):
    if i!=N-1:
        i=j
    for j in range(i-1, -1, -1):
        if alunos[i]>alunos[j]:
            colas+=1
        else:
            break
    if(j==0):
        break
print(colas)