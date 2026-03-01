N = int(input())
K = int(input())
nota = []
for i in range(N):
    nota.append(int(input()))
nota.sort()
print(nota[N-K])