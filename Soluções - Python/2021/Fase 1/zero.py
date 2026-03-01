N = int(input())
lista = []
for i in range(N):
    X = int(input())
    if X!=0:
        lista.append(X)
    else:
        lista.pop()
print(sum(lista))