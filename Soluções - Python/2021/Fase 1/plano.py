X = int(input())
N = int(input())
meses = []
for i in range(N):
    meses.append(int(input()))
print(X*(N+1)-sum(meses))