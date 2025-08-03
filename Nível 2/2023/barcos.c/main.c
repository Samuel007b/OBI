#include <stdio.h>
int main()
{
    int a=0, i, j, k, n, b, c;
    scanf("%i%i", &n, &b); // N -> número de ilhas, B -> número de barcos
    const int N = n;
    const int B = b;
    int ilhas[N];
    for(i=1; i<=N; i++)
    {
        ilhas[i]=i;
    }
    int ilha1[B];
    int ilha2[B];
    int passageiros[B];
    for(i=1; i<=B; i++)
    {
        scanf("%i", &ilha1[i]);
        scanf("%i", &ilha2[i]);
        scanf("%i", &passageiros[i]);
    }
    scanf("%i", &c); // C -> número de consultas
    const int C = c;
    int partida[C];
    int chegada[C];
    for(i=1; i<=C; i++)
    {
        scanf("%i", &partida[i]);
        scanf("%i", &chegada[i]);
    }
    int pessoas[C];
    int trajeto[C][N][N];
    for(i=1; i<=C; i++)
    {
        pessoas[i]=0;
    }
    for(i=1; i<=C; i++)
    {
        for(j=1; j<=N; j++)
        {
            if(partida[i]==ilha[j])
            {
                a++
                trajeto[i][a] = j;
                for(k=1; k<=B; k++)
                {
                    if(partida[i]==ilha1[k])
                    {
                        a++;
                        trajeto[i][a] = ilha2[k];
                    }
                    if(partida[i]==ilha2[k])
                    {
                        
                    }
                }
            }
        }
    }
    for(i=1; i<=C; i++)
    {
        for(j=1; j<=N; j++)
        {
            if(partida[i]==ilha[j])
            {
                for(k=1; k<=B; k++)
                {
                    if(partida[i]==ilha1[k])
                    {
                        if(passageiros[k]>pessoas[i])
                            pessoas[i]=passageiros[k];
                    }
                    if(partida[i]==ilha2[k])
                    {
                        if(passageiros[k]>pessoas[i])
                            pessoas[i]=passageiros[k];
                    }
                }
            }
        }
        printf("%i", pessoas[i]);
    }
    
    

    return 0;
}