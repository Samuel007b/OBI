N = int(input())
lances = []
nomes = []
for i in range(N):
    nomes.append(input())
    lances.append(int(input()))
maior = 0
venc = -1
for i in range(N):
    if lances[i] > maior:
        maior = lances[i]
        venc = i
print(f'{nomes[venc]}\n{lances[venc]}')