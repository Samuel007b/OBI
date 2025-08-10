#include <stdio.h>
int main()
{
    int i, j, N, Q, a, b;
    scanf("%i%i", &N, &Q);
    int lista[N];
    int potencial[Q];
    int intervalo;
    for(i=1; i<=N; i++)
    {
        scanf("%i", &lista[i]);
    }
    for(i=1; i<=Q; i++)
    {
        intervalo=0;
        scanf("%i%i", &a, &b);
        for(j=a; j<=b; j++)
        {
            intervalo+=lista[j];
        }
        intervalo*=11*(b-a);
        potencial[i]=intervalo;
    }
    for(i=1; i<=Q; i++)
    {
        printf("%i\n", potencial[i]);
    }
    return 0;
}