D = int(input())
A = int(input())
N = int(input())
diaria = []
for i in range(31):
    if i<15:
        diaria.append((31-i)*(D+i*A))
    else:
        diaria.append((31-i)*(D+14*A))
print(diaria[N-1])