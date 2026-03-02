P = int(input())
golsP = []
for i in range(P):
    golsP.append(int(input()))
C = int(input())
golsC = []
for i in range(C):
    golsC.append(int(input()))
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