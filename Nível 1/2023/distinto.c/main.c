#include <stdio.h>
int main()
{
    int erro, i, j, k, n;
    scanf("%i", &n);
    const int N = n;
    int sequencia[N], distinto[N];
    for(i=0; i<N; i++)
        scanf("%i", &sequencia[i]);
    for(i=0; i<N; i++)
    {
        erro=0;
        distinto[i]=1;
        for(j=i; j<N; j++)
        {
            for(k=j-1; k>=i; k--)
            {
                if(sequencia[j]!=sequencia[k])
                {
                    if(k==i)
                        distinto[i]++;
                }
                else
                {
                    erro=1;
                    break;
                }
            }
            if(erro==1)
                break;
        }
    }
    int maior = distinto[0];
    for(i=0; i<N; i++)
    {
        if(distinto[i]>maior)
            maior=distinto[i];
    }
    printf("%i", maior);
    return 0;
}