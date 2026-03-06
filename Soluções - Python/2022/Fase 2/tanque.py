# OBI 2022 - Fase 2 - Níveis 1 e Sênior
# Questão: Tanque de combustível

C = int(input())
D = int(input())
T = int(input())
litros = D/C - T
if litros<0:
    litros=0
print(f"{litros:.1f}")