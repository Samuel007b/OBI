N = int(input())
P = int(input())
dias = 0
bact = 1
while True:
    bact *= P
    if bact>N:
        break
    else:
        dias += 1
print(dias)