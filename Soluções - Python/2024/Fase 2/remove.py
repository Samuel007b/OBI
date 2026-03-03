# OBI 2024 - Fase 2 - Nível 2 (Turno B)
# Questão: Remove Dígitos

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