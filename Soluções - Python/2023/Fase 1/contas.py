V = int(input())
contas = []
divida = 0
pagamentos = 0
for i in range(3):
    contas.append(int(input()))
contas.sort()
for i in range(3):
    divida += contas[i]
    if(V>=divida):
        pagamentos += 1
    else:
        break
print(pagamentos)