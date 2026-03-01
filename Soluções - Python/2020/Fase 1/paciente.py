N = int(input())
C = int(input())
cadeias = []
pacZero1 = []
for i in range(C):
    cadeia = []
    P = int(input())
    pacZero1.append(P)
    I = int(input())
    for j in range(I):
        cadeia.append(int(input()))
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