R = int(input())
N = int(input())
tabela1 = []
tabela2 = []
tabela3 = []
for i in range(N):
    fruta = []
    fruta.append(int(input()))
    fruta.append(int(input()))
    tabela1.append(fruta)
    tabela2.append(fruta)
for i in range(N):
    for j in range(N):
        if i!=j and tabela1[i][0]==tabela1[j][0]:
            if tabela1[i][1]<tabela1[j][1]:
                if tabela1[j] in tabela2:
                    tabela2.pop(tabela2.index(tabela1[j]))
for i in range(len(tabela2)):
    if tabela2[i] not in tabela3:
        tabela3.append(tabela2[i])
frutas = []
gasto = 0
while True:
    if len(tabela3)!=0:
        menor = tabela3[0]
        for i in range(len(tabela3)):
            if tabela3[i][1]<menor[1]:
                menor=tabela3[i]
        if gasto+menor[1]<=R:
            gasto+=menor[1]
            frutas.append(menor)
            tabela3.pop(tabela3.index(menor))
        else:
            break
    else:
        break
print(len(frutas))