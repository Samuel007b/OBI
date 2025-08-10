#include <stdio.h>

int main()
{
    int i, j, K, N, acertos=0;
    scanf("%i%i%*c", &K, &N);
    char alfabeto[K+1], mensagem[N+1];
    for(i=1; i<=K; i++)
    {
        scanf("%c", &alfabeto[i]);
    }
    getchar();
    for(i=1; i<=N; i++)
    {
        scanf("%c", &mensagem[i]);
    }
    getchar();
    for(i=1; i<=N; i++)
    {
        for(j=1; j<=K; j++)
        {
            if(mensagem[i]==alfabeto[j])
                acertos++;
        }
    }
    if(acertos==N)
        printf("S");
    else
        printf("N");
    return 0;
}