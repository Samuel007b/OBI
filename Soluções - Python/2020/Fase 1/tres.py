N = int(input())
precos = []
for i in range(N):
    precos.append(int(input()))
precos.sort()
for i in range(1, N, 1):
    if N-3*i>=0:
        precos.pop(N-3*i)
    else:
        break
print(sum(precos))