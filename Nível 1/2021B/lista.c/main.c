#include <stdio.h>
int main()
{
    int i, a, n, meio, contracoes=0;
    scanf("%i", &n);
    const int N = n;
    meio = N/2;
    int lista[N];
    getchar();
    for(i=0; i<N; i++)
    {
        scanf("%i", &lista[i]);
    }
    for(i=0; i<meio; i++)
    {
        a=N-i-1;
        if(lista[i]!=lista[a])
            contracoes++;
    }
    printf("%i", contracoes);
    return 0;
}