N = int(input())
M = int(input())
quantCal = 0
for i in range(N):
    P = int(input())
    G = int(input())
    C = int(input())
    quantCal += 4*P + 9*G + 4*C
print(M-quantCal)