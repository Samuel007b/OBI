#include <stdio.h>
int main()
{
    int i, j, K, N, contador=0;
    scanf("%i%i", &K, &N);
    char alfabeto[K], mensagem[N];
    getchar();
    for(i=0; i<K; i++)
    {
        scanf("%c", &alfabeto[i]);
    }
    getchar();
    for(i=0; i<N; i++)
    {
        scanf("%c", &mensagem[i]);
    }
    for(i=0; i<N; i++)
    {
        for(j=0; j<K; j++)
        {
            if(mensagem[i]==alfabeto[j])
                break;
            else if(j==K-1)
                contador++;
        }
        if(contador>0)
        {
            printf("N");
            break;
        }
        else if(i==N-1)
            printf("S");
    }
    return 0;
}