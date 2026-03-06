# OBI 2022 - Fase 2 - Níveis 2 e Sênior
# Questão: Subcadeias

N = int(input())
C = input()
subcadeiaI = []
for i in range(len(C)):
    palindromo = 1
    a=0
    while True:
        a+=1
        if i-a>=0 and i+a<len(C) and C[i-a]==C[i+a]:
            palindromo += 2
        else:
            break
    subcadeiaI.append(palindromo)
subcadeiaP = []
for i in range(len(C)-1):
    if C[i]==C[i+1]:
        palindromo = 2
        a=0
        while True:
            a+=1
            if i-a>=0 and i+1+a<len(C) and C[i-a]==C[i+1+a]:
                palindromo += 2
            else:
                break
        subcadeiaP.append(palindromo)
if len(subcadeiaI)==0:
    print(max(subcadeiaP))
elif len(subcadeiaP)==0:
    print(max(subcadeiaI))
else:
    if max(subcadeiaI)>max(subcadeiaP):
        print(max(subcadeiaI))
    else:
        print(max(subcadeiaP))