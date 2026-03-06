# OBI 2020 - Fase 2 - Nível Júnior
# Questão: Jogo dos Pinos

tabuleiro = []
for i in range(7):
    tabuleiro.append(input())
movimentos = 0
for i in range(7):
    for j in range(7):
        if tabuleiro[i][j]=='o':
            if i+1<7 and i+2<7 and tabuleiro[i+1][j]=='o' and tabuleiro[i+2][j]=='.':
                movimentos+=1
            if i-1>=0 and i-2>=0 and tabuleiro[i-1][j]=='o' and tabuleiro[i-2][j]=='.':
                movimentos+=1
            if j+1<7 and j+2<7 and tabuleiro[i][j+1]=='o' and tabuleiro[i][j+2]=='.':
                movimentos+=1
            if j-1>=0 and j-2>=0 and tabuleiro[i][j-1]=='o' and tabuleiro[i][j-2]=='.':
                movimentos+=1
print(movimentos)