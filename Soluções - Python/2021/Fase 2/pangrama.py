# OBI 2021 - Fase 2 - Nível Júnior (Turno A)
# Questão: Pangrama

C = input()
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
for i in range(len(C)):
    if C[i] in alfabeto:
        alfabeto.pop(alfabeto.index(C[i]))
if len(alfabeto)==0:
    print('S')
else:
    print('N')