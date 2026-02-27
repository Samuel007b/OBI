#include <stdio.h>
int main()
{
    int i, n, c, s, estacao_atual=1, vezes=0;
    scanf("%i%i%i", &n, &c, &s);
    const int N = n;
    const int C = c;
    const int S = s;
    int comando[C];
    getchar();
    for(i=0; i<C; i++)
    {
        scanf("%i", &comando[i]);
    }
    if(S==1)
        vezes++;
    for(i=0; i<C; i++)
    {
        if(comando[i]==1)
        {
            if(estacao_atual==N)
                estacao_atual=1;
            else
                estacao_atual+=1;
        }
        else if(comando[i]==-1)
        {
            if(estacao_atual==1)
                estacao_atual=N;
            else
                estacao_atual-=1;
        }
        if(estacao_atual==S)
            vezes++;
    }
    printf("%i", vezes);
    return 0;
}