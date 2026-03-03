# OBI 2021 - Fase 1 - Nível 2
# Questão: Cifra da Nlogônia

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']

def isVogal(caracter):
    for i in vogais:
        if caracter == i:
            return True
    return False

def nextConsoante(caracter):
    if caracter=='z':
        return 'z'
    else:
        for i in range(len(consoantes)):
            if caracter == consoantes[i]:
                return consoantes[i+1]

def nextVogal(caracter):
    for i in range(len(alfabeto)):
        if caracter == alfabeto[i]:
            j = i+1
            while True:
                if isVogal(alfabeto[j]) == True:
                    vogal1 = alfabeto[j]
                    break
                j += 1
                if j==len(alfabeto):
                    j=-1
                    break
            k = i-1
            while True:
                if isVogal(alfabeto[k]) == True:
                    vogal2 = alfabeto[k]
                    break
                k -= 1
                if k==-1:
                    break
            if j==-1:
                return vogal2
            elif k==-1:
                return vogal1
            else:
                if j-i<i-k:
                    return vogal1
                else:
                    return vogal2
            break

P = input()
newP = []
for caracter in P:
    newP.append(caracter)
    if isVogal(caracter) == False:
        newP.append(nextVogal(caracter))
        newP.append(nextConsoante(caracter))
for caracter in newP:
    print(caracter, end='')