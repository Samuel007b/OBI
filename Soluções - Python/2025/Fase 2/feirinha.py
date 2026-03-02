N = int(input())
obj1 = []
obj2 = []
for i in range(N):
    t = int(input())
    if t==1:
        obj1.append(i)
    else:
        obj2.append(i)
precos = []
pre1 = []
pre2 = []
for i in range(N):
    p = int(input())
    precos.append(p)
    if i in obj1:
        pre1.append(p)
    else:
        pre2.append(p)
C = int(input())
lucro = 0
for i in range(C):
    c = int(input())
    if c==1 and len(pre1)>0:
        lucro += min(pre1)
        obj1.pop(pre1.index(min(pre1)))
        precos.pop(precos.index(min(pre1)))
        pre1.pop(pre1.index(min(pre1)))
    elif c==2 and len(pre2)>0:
        lucro += min(pre2)
        obj2.pop(pre2.index(min(pre2)))
        precos.pop(precos.index(min(pre2)))
        pre2.pop(pre2.index(min(pre2)))
    elif c==0 and len(precos)>0:
        lucro += min(precos)
        if min(precos) in pre1:
            pre1.pop(pre1.index(min(precos)))
        else:
            pre2.pop(pre2.index(min(precos)))
        precos.pop(precos.index(min(precos)))
print(lucro)