N = int(input())
p = 0
m = 0
for i in range(N):
    t = int(input())
    if t==1:
        p+=1
    elif t==2:
        m+=1
P = int(input())
M = int(input())
if p==P and m==M:
    print('S')
else:
    print('N')