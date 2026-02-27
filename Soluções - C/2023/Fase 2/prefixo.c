#include <stdio.h>
int main()
{
    int i, n, m, contador=0;
    scanf("%i", &n);
    const int N = n;
    char palavra1[N];
    getchar();
    for(i=0; i<N; i++)
    {
        scanf("%c", &palavra1[i]);
    }
    scanf("%i", &m);
    const int M = m;
    char palavra2[M];
    getchar();
    for(i=0; i<M; i++)
    {
        scanf("%c", &palavra2[i]);
    }
    for(i=0; i<M; i++)
    {
        if(palavra1[i]==palavra2[i])
            contador++;
        else
            break;
    }
    printf("%i", contador);
    return 0;
}