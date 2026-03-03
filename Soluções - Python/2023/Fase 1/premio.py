# OBI 2023 - Fase 1 - Nível Júnior
# Questão: Prêmio

P = int(input())
D = int(input())
B = int(input())
pts = P + 2*D + 3*B
if pts>=150:
    print('B')
elif pts>=120:
    print('D')
elif pts>=100:
    print('P')
else:
    print('N')