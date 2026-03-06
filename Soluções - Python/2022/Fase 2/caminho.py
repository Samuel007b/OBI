# OBI 2022 - Fase 2 - Nível Júnior
# Questão: Caminho

N = int(input())
lampadas = []
for i in range(N):
    lampadas.append(int(input()))
trechos = []
for i in range(N):
    if i==N-1:
        if lampadas[i]+lampadas[0]<1000:
            trechos.append(i)
    else:
        if lampadas[i]+lampadas[i+1]<1000:
            trechos.append(i)
if len(trechos)>0:
    trechosEscuros = []
    for i in range(len(trechos)):
        escuro = 1
        a=i+1
        b=a-1
        while True:
            if escuro==len(trechos):
                break
            if a==len(trechos):
                a=0
                if trechos[a]==0 and trechos[b]==len(lampadas)-1:
                    escuro+=1
                    a+=1
                    b=a-1
                else:
                    break
            elif trechos[a]==trechos[b]+1:
                escuro+=1
                a+=1
                b=a-1
            else:
                break
        trechosEscuros.append(escuro)
    print(max(trechosEscuros))
else:
    print('0')