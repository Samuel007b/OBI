A = int(input())
B = int(input())
Sa = []
Sb = []
b = 0
for i in range(A):
    Sa.append(int(input()))
for i in range(B):
    Sb.append(int(input()))
for a in range(A):
    if Sa[a] == Sb[b]:
        b+=1
if b==B:
    print('S')
else:
    print('N')