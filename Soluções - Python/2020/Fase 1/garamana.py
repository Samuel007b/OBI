# OBI 2020 - Fase 1 - Nível Sênior (Turno B)
# Questão: Garamana

P = input()
letras = []
for let in P:
    letras.append(let)
A = input()
erro = False
for i in range(len(A)):
    if A[i] not in letras and A[i]!='*':
        erro=True
        break
    elif A[i]!='*':
        letras.pop(letras.index(A[i]))
if erro==False:
    print('S')
else:
    print('N')