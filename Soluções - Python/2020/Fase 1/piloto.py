carros = []
for i in range(3):
    carros.append(int(input()))
if carros[2]-carros[1]>carros[1]-carros[0]:
    print('1')
elif carros[2]-carros[1]<carros[1]-carros[0]:
    print('-1')
else:
    print('0')