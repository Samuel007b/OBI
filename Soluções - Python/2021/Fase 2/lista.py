# OBI 2021 - Fase 2 - Níveis 1, 2 e Sênior (Turno B)
# Questão: Lista Palíndroma

N = int(input())
lista = list(map(int, input().split()))
while True:
    erro = False
    if len(lista)%2==0:
        for i in range(int(len(lista)/2)):
            if lista[i] != lista[len(lista)-i-1]:
                erro = True
                break
    else:
        for i in range(int((len(lista)-1)/2)):
            if lista[i] != lista[len(lista)-i-1]:
                erro = True
                break
    if erro == False:
        print(N-len(lista))
        break
    else:
        if len(lista)%2==0:
            for i in range(int(len(lista)/2)):
                if lista[i]>lista[len(lista)-i-1]:
                    lista[len(lista)-i-1]+=lista[len(lista)-i-2]
                    lista.pop(len(lista)-i-2)
                    break
                elif lista[i]<lista[len(lista)-i-1]:
                    lista[i]+=lista[i+1]
                    lista.pop(i+1)
                    break
        else:
            for i in range(int((len(lista)-1)/2)):
                if lista[i]>lista[len(lista)-i-1]:
                    lista[len(lista)-i-1]+=lista[len(lista)-i-2]
                    lista.pop(len(lista)-i-2)
                    break
                elif lista[i]<lista[len(lista)-i-1]:
                    lista[i]+=lista[i+1]
                    lista.pop(i+1)
                    break