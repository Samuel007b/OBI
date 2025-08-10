#include <stdio.h>

int main()
{
    int i, j, R, N, frutas, total, barato;
    scanf("%i%i", &R, &N);
    int tabela[N][2];
    for(i=1; i<=N; i++)
    {
        scanf("%i", &tabela[i][1]); // tipo de fruta
        scanf("%i", &tabela[i][2]); // preço
    }
    barato=tabela[1][2];
    for(i=1; i<=N; i++)
    {
        if(tabela[i][2]<barato)
            barato=tabela[i][2];
    }
    
    printf("%i", barato);
    return 0;
}