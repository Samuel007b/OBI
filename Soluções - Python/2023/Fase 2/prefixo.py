N = int(input())
palavra1 = input()
M = int(input())
palavra2 = input()
i=0
while True:
    if i==N or i==M:
        break
    else:
        if palavra1[i]==palavra2[i]:
            i+=1
        else:
            break
print(i)