# OBI 2026 - Fase 1 (Turno B) - Níveis Júnior, 1 e Sênior
# Questão: Fichas

X = int(input())
fichas=0
fichas+=int(X/10)
X-=int(X/10)*10
fichas+=int(X/5)
X-=int(X/5)*5
fichas+=int(X/2)
X-=int(X/2)*2
fichas+=X
print(fichas)