N = int(input())
K = int(input())
alfAli = input()
msg = input()
erro = False
for let in msg:
    if let not in alfAli:
        print('N')
        erro=True
        break
if erro==False:
    print('S')