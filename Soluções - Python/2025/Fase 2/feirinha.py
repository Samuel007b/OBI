# OBI 2025 - Fase 2 - Níveis Júnior, 1, 2 e Sênior
# Questão: Feirinha de Artesanato

N = int(input())
obj0 = list(map(int, input().split()))
obj1 = []
obj2 = []
for i in range(N):
    if obj0[i]==1:
        obj1.append(i)
    else:
        obj2.append(i)
precos = list(map(int, input().split()))
pre1 = []
pre2 = []
for i in range(N):
    if i in obj1:
        pre1.append(precos[i])
    else:
        pre2.append(precos[i])
C = int(input())
clientes = list(map(int, input().split()))
lucro = 0
for i in range(C):
    if clientes[i]==1 and len(pre1)>0:
        lucro += min(pre1)
        obj1.pop(pre1.index(min(pre1)))
        precos.pop(precos.index(min(pre1)))
        pre1.pop(pre1.index(min(pre1)))
    elif clientes[i]==2 and len(pre2)>0:
        lucro += min(pre2)
        obj2.pop(pre2.index(min(pre2)))
        precos.pop(precos.index(min(pre2)))
        pre2.pop(pre2.index(min(pre2)))
    elif clientes[i]==0 and len(precos)>0:
        lucro += min(precos)
        if min(precos) in pre1:
            pre1.pop(pre1.index(min(precos)))
        else:
            pre2.pop(pre2.index(min(precos)))
        precos.pop(precos.index(min(precos)))
print(lucro)