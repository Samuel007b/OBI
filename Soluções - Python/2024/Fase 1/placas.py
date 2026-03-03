# OBI 2024 - Fase 1 - Nível Sênior
# Questão: Placas de Carro

placa = input()
if len(placa)==7:
    if placa[0].isupper() and placa[1].isupper() and placa[2].isupper() and placa[3].isalnum and placa[4].isupper() and placa[5].isalnum and placa[6].isalnum:
        print('2')
    else:
        print('0')
elif len(placa)==8:
    if placa[0].isupper() and placa[1].isupper() and placa[2].isupper() and placa[3]=='-' and placa[4].isalnum and placa[5].isalnum and placa[6].isalnum and placa[7].isalnum:
        print('1')
    else:
        print('0')
else:
    print('0')