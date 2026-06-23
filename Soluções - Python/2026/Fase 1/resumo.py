# OBI 2026 - Fase 1 (Turno B) - Níveis 2 e Sênior
# Questão: Resumo de Números

N = int(input())
chatos = [N]
while True:
    N = str(N)
    algarismos = []
    par = 0
    for alg in N:
        algarismos.append(int(alg))
        if (int(alg)%2==0):
            par+=1
    N = len(algarismos)*100+(len(algarismos)-par)*10+par
    if N in chatos:
        break
    else:
        chatos.append(N)
print(len(chatos)-1)