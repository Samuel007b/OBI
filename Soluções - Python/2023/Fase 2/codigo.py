# OBI 2023 - Fase 2 - Níveis Júnior e 2
# Questão: Código de Compressão

N = int(input())
caracteres = input()
for i in range(len(caracteres)):
    if i==0 or caracteres[i]!=caracteres[i-1]:
        a=i+1
        while True:
            if a>=len(caracteres) or caracteres[a]!=caracteres[a-1]:
                break
            else:
                a+=1
        print(f"{a-i} {caracteres[i]}", end=" ")