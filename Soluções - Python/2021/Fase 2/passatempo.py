# OBI 2021 - Fase 2 - Níveis 2 e Sênior (Turno A)
# Questão: Passatempo

L, C = map(int, input().split())
passatempo = []
Sx = []
for i in range(L):
    lin = input()
    line = []
    for j in range(len(lin)):
        if lin[j]!=" ":
            line.append(lin[j])
    print(line)
    linha = []
    while line[0].isalpha:
        linha.append((line[0]+line[1]))
        line.pop(0)
    passatempo.append(linha)
    Sx.append(int(line))
Sy = list(map(int, input().split()))

for i in range(L):
    for j in range(C):
        print(passatempo[i][j], end=" ")
    print()
print(Sx)
print(Sy)

# a fazer