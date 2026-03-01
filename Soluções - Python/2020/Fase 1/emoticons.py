M = input()
divertido = 0
chateado = 0
for i in range(0, len(M)-2, 1):
    if M[i]==':' and M[i+1]=='-':
        if M[i+2]==')':
            divertido+=1
        elif M[i+2]=='(':
            chateado+=1
if divertido>chateado:
    print('divertido')
elif divertido<chateado:
    print('chateado')
else:
    print('neutro')