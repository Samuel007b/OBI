# OBI 2024 - Fase 2 - Níveis Júnior e 1
# Questão: Avenida

D = int(input())
if D%400>200:
    print(400-D%400)
else:
    print(D%400)