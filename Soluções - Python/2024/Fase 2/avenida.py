D = int(input())
if D%400>200:
    print(400-D%400)
else:
    print(D%400)