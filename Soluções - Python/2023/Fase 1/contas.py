# OBI 2023 - Fase 1 - Níveis 2 e Sênior
# Questão: Contas a Pagar

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