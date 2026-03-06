# OBI 2021 - Fase 2 - Nível Júnior (Turno B)
# Questão: Anagrama

N = int(input())
A = input()
fraseA = []
for i in range(len(A)):
    fraseA.append(A[i])
B = input()
erro = False
for i in range(len(B)):
    if B[i] in fraseA:
        fraseA.pop(fraseA.index(B[i]))
    else:
        print('N')
        erro = True
        break
if erro==False:
    print('S')