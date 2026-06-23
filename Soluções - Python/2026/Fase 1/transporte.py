# OBI 2026 - Fase 1 (Turno B) - Níveis 1, 2 e Sênior
# Questão: Transporte

N, T = map(int, input().split())
t = list(map(int, input().split()))
onibus = 0
passageiros = []
for i in range(len(t)):
    if t[i] in passageiros:
        continue
    else:
        onibus+=1
        passageiros.append(t[i])
        for j in range(i+1, len(t)):
            if (t[j]-t[i])<=T:
                passageiros.append(t[j])
            else:
                break
print(onibus)