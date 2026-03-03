# OBI 2024 - Fase 2 - Níveis Júnior, 1, 2 e Sênior
# Questão: Alfabeto Alienígena

N, K = map(int, input().split())
alfAli = input()
msg = input()
erro = False
for let in msg:
    if let not in alfAli:
        print('N')
        erro=True
        break
if erro==False:
    print('S')