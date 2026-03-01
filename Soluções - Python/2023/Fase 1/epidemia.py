N = int(input())
R = int(input())
P = int(input())
dias = 0
ativo = N
while True:
    if(N>=P):
        break
    else:
        ativo *= R
        N += ativo
        dias += 1
print(dias)