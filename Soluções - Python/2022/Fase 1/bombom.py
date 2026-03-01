def valorCarta(carta, pts):
    match carta[0]:
        case 'A':
            if carta[1]==naipeDom:
                pts += 14
            else:
                pts += 10
        case 'J':
            if carta[1]==naipeDom:
                pts += 15
            else:
                pts += 11
        case 'Q':
            if carta[1]==naipeDom:
                pts += 16
            else:
                pts += 12
        case 'K':
            if carta[1]==naipeDom:
                pts += 17
            else:
                pts += 13
    return pts

tombo = input()
naipeDom = tombo[1]
Lpts = 0
for i in range(3):
    carta = input()
    Lpts = valorCarta(carta, Lpts)
Epts = 0
for i in range(3):
    carta = input()
    Epts = valorCarta(carta, Epts)
if Lpts>Epts:
    print('Luana')
elif Lpts<Epts:
    print('Edu')
else:
    print('empate')