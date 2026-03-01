idade = []
preco = 0
for i in range(2):
    idade.append(int(input()))
    if idade[i]<=17:
        preco += 15
    elif idade[i]<60:
        preco += 30
    else:
        preco += 20
print(preco)