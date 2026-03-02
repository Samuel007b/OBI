N = int(input())
G = int(input())
M = int(input())
sobra = (8*G+6*M)-N
if sobra<0:
    print('0')
else:
    print(sobra)