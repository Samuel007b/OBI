# OBI 2020 - Fase 2 - Níveis 1, 2 e Sênior
# Questão: Estrada

T = int(input())
N = int(input())
cidades = []
for i in range(N):
    cidades.append(int(input()))
cidades.sort()
vizinhancas = []
for i in range(N):
    if i==0:
        vizinhancas.append(cidades[0]+(cidades[1]-cidades[0])/2)
    elif i==N-1:
        vizinhancas.append(T-cidades[N-1]+(cidades[N-1]-cidades[N-2])/2)
    else:
        vizinhancas.append((cidades[i]-cidades[i-1])/2+(cidades[i+1]-cidades[i])/2)
print(f"{min(vizinhancas):.2f}")