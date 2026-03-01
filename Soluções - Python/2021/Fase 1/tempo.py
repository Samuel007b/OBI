N = int(input())
registro = []
amigo = []
periodo = []
tempo = 0
for i in range(N):
    caractere = input()
    num = int(input())
    match caractere:
        case 'R' | 'E':
            registro.append(caractere)
            amigo.append(num)
            periodo.append(tempo)
        case 'T':
            tempo += num-1
    tempo +=1
# a fazer