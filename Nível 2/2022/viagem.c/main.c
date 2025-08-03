#include <stdio.h>

int main()
{
    int i, j, a, v, n, m, x, y, ilha_atual, fim, melhor;
    scanf("%i%i%i", &v, &n, &m);
    const int V = v; // valor esperado
    const int N = n; // Nº de ilhas
    const int M = m; // Nº de viagens
    int ilha1[M], ilha2[M], tempo[M], custo[M];
    for(i=0; i<M; i++)
    {
        scanf("%i", &ilha1[i]);
        scanf("%i", &ilha2[i]);
        scanf("%i", &tempo[i]);
        scanf("%i", &custo[i]);
    }
    scanf("%i%i", &x, &y);
    const int X = x; // ilha de partida
    const int Y = y; // ilha de chegada
    int tp[M], ct[M];
    for(j=0; j<M; j++)
    {
        tp[j] = ct[j] = 0;
        ilha_atual = X;
        fim=0;
        a=0;
        for(;;)
        {
            for(i=0; i<M; i++)
            {
                if(ilha1[i]==ilha_atual)
                {
                    tp[i]+=tempo[i];
                    ct[i]+=custo[i];
                    if(ilha2[i]==Y)
                    {
                        fim = 1;
                        break;
                    }
                    else
                        ilha_atual=ilha2[i];
                }
                else if(ilha2[i]==ilha_atual)
                {
                    tp[i]+=tempo[i];
                    ct[i]+=custo[i];
                    if(ilha1[i]==Y)
                    {
                        fim = 1;
                        break;
                    }
                    else
                        ilha_atual=ilha2[i];
                }
            }
            if(fim==1)
                break;
        }
    }
    for(j=0; j<M; j++)
    {
        if(ct[j]<=V)
        {
            melhor=tp[j];
            break;
        }
    }
    for(j=0; j<M; j++)
    {
        if(ct[j]<=V && tp[j]<melhor)
            melhor=tp[j];
    }
    if(melhor==0)
        printf("-1");
    else
        printf("%i", melhor);
    return 0;
}