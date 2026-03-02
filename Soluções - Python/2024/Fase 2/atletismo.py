N = int(input())
ordem = []
for i in range(N):
    ordem.append(int(input()))
for i in range(N):
    print(ordem.index(i+1)+1)