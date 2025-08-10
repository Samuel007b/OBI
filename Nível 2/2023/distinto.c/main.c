#include <stdio.h>

int main()
{
    int i, j, k, n, N, maior, erro;
    scanf("%i", &N);
    n=N;
    int lista[n];
    int sequencia[n];
    for(i=1; i<=N; i++)
    {
        scanf("%i", &lista[i]);
    }
    for(i=1; i<=N; i++)
    {
        sequencia[i]=1;
        erro=0;
        for(j=i+1; j<=N; j++)
        {
            for(k=i; k<=j-1; k++)
            {
                if(lista[j]!=lista[k])
                {
                    if(k==(j-1))
                        sequencia[i]++;
                }
                else if(lista[j]==lista[k])
                {
                    erro=1;
                    break;
                }
            }
            if(erro==1)
                break;
        }
    }
    maior=sequencia[1];
    for(i=2; i<=N; i++)
    {
        if(maior<sequencia[i])
            maior=sequencia[i];
    }
    printf("%i", maior);
    return 0;
}