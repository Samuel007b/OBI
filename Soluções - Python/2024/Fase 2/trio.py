N = int(input())
palitos = []
for i in range(N):
    palitos.append(int(input()))
trios = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i!=j and j!=k and i!=k:
                if palitos[i]+palitos[j]>palitos[k] and palitos[i]+palitos[k]>palitos[j] and palitos[j]+palitos[k]>palitos[i]:
                    trios+=1
print(int(trios/6))