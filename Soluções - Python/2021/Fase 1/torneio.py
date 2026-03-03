# OBI 2021 - Fase 1 - Níveis Júnior, 1 e Sênior
# Questão: Torneio de Tênis

vit = 0
for i in range(6):
    jogo = input()
    if jogo=='V':
        vit += 1
match vit:
    case 0:
        print('-1')
    case 1|2:
        print('3')
    case 3|4:
        print('2')
    case 5|6:
        print('1')