# OBI 2022 - Fase 2 - Níveis Júnior e 2
# Questão: Troféu

pontuacao = []
for i in range(5):
    pontuacao.append(int(input()))
pontos = pontuacao.copy()
trofeu = 0
placa = 0
nota1 = max(pontuacao)
for i in range(5):
    if pontuacao[i]==nota1:
        trofeu+=1
        pontos.pop(pontos.index(pontuacao[i]))
if len(pontos)>0:
    nota2 = max(pontos)
    for i in range(len(pontos)):
        if pontos[i]==nota2:
            placa+=1
print(f"{trofeu} {placa}")