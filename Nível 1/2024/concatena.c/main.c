#include <stdio.h>
int main()
{
    int a, b, i, j, n, q, contador;
    scanf("%i%i", &n, &q);
    const int N = n;
    const int Q = q;
    int lista[N];
    int perg1[Q], perg2[Q];
    getchar();
    for(i=0; i<N; i++)
    {
        scanf("%i", &lista[i]);
    }
    getchar();
    for(i=0; i<Q; i++)
    {
        scanf("%i", &perg1[i]);
        scanf("%i", &perg2[i]);
    }
    for(i=0; i<Q; i++)
    {
        contador=0;
        a=perg1[i];
        b=perg2[i];
        for(j=a; j<=b; j++)
        {
            contador+=lista[j-1];
        }
        contador*=11*(b-a);
        printf("%i\n", contador);
    }
    return 0;
}