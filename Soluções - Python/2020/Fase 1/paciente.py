# OBI 2020 - Fase 1 - Nível Sênior (Turno A)
# Questão: Paciente Zero

N, C = map(int, input().split())
cadeias = []
pacZero1 = []
for i in range(C):
    cadeia = list(map(int, input().split()))
    pacZero1.append(cadeia[0])
    cadeia.pop(0)
    cadeia.pop(0)
    cadeias.append(cadeia)
pacZero2 = pacZero1.copy()
pacZero2.sort()
for i in range(len(pacZero1)):
    for j in range(C):
        if pacZero1[i] in cadeias[j]:
            pacZero2.pop(pacZero2.index(pacZero1[i]))
            break
for pac in pacZero2:
    print(pac)