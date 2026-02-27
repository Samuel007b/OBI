N = int(input())
brinq = []
for i in range(N):
    brinq.append(int(input()))
for i in range(max(brinq), 0, -1):
    for j in range(N):
        if brinq[j]>=i:
            print('1', end=" ")
        else:
            print('0', end=" ")
    print()