# OBI 2026 - Fase 1 - Níveis Júnior, 2 e Sênior
# Questão: Restaurante

G1, G2, G3, G4 = map(int, input().split())
mesas = G4 + G3
if(G1<=G3):
    if(G2%2==0):
        mesas += int(G2/2)
    else:
        mesas += int(G2/2) + 1
else:
    G1-=G3
    if(G2%2==0):
        mesas += int(G2/2)
        if(G1%4==0):
            mesas += int(G1/4)
        else:
            mesas += int(G1/4) + 1
    else:
        mesas += int(G2/2) + 1
        G1 -= 2
        if(G1>0):
            if(G1%4==0):
                mesas += int(G1/4)
            else:
                mesas += int(G1/4) + 1
print(mesas)