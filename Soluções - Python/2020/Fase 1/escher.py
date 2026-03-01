N = int(input())
colunas = []
for i in range(N):
    colunas.append(int(input()))
soma = colunas[0]+colunas[N-1]
erro = False
if N%2==0:
    for i in range(int(N/2)):
        if colunas[i]+colunas[N-1-i] != soma:
            erro = True
            break
else:
    for i in range(int((N-1)/2)):
        if colunas[i]+colunas[N-1-i] != soma:
            erro = True
            break
    if colunas[int((N+1)/2)-1]*2 != soma:
        erro = True
if erro == True:
    print('N')
else:
    print('S')