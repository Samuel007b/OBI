#include <stdio.h>
int main()
{
    int i, s, t, p, saloes=-1;
    scanf("%i%i%i", &s, &t, &p);
    const int S = s;
    const int T = t;
    const int P = p;
    int altura[S];
    int tuneis[T][2];
    getchar();
    for(i=0; i<S; i++)
    {
        scanf("%i", &altura[i]);
    }
    getchar();
    for(i=0; i<T; i++)
    {
        scanf("%i%i", &tuneis[i][0], &tuneis[i][1]);
    }
    for(i=0; i<S; i++)
    {
        if(altura[i]<=altura[P-1])
            saloes++;
    }
    printf("%i", saloes);
    return 0;
}