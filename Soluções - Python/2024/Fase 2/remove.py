N = int(input())
rodadas = 0
while True:
    if N==0:
        break
    else:
        casas = []
        for i in range(6):
            casas.append(int(N/10**i)%10)
        N-=max(casas)
        rodadas+=1
print(rodadas)