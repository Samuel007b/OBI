# OBI 2021 - Fase 1 - Nível Sênior
# Questão: Baralho

baralho = input()
copas = []
espadas = []
ouros = []
paus = []

def repeteCarta(cartas):
    for i in range(len(cartas)):
        for j in range(i+1, len(cartas), 1):
            if cartas[i]==cartas[j]:
                return True
    return False

def resultado(cartas):
    if repeteCarta(cartas)==True:
        print('erro')
    else:
        print(13-len(cartas))

for i in range(len(baralho)):
    if i%3==2:
        match baralho[i]:
            case 'C':
                copas.append(int(baralho[i-2]+baralho[i-1]))
            case 'E':
                espadas.append(int(baralho[i-2]+baralho[i-1]))
            case 'U':
                ouros.append(int(baralho[i-2]+baralho[i-1]))
            case 'P':
                paus.append(int(baralho[i-2]+baralho[i-1]))
resultado(copas)
resultado(espadas)
resultado(ouros)
resultado(paus)