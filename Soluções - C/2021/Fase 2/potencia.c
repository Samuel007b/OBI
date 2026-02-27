#include <stdio.h>
#include <math.h>
int main()
{
    int i, a, b, N, soma=0;
    scanf("%i", &N);
    int potencias[N];
    getchar();
    for(i=0; i<N; i++)
    {
        scanf("%i", &potencias[i]);
        a=potencias[i]/10;
        b=potencias[i]%10;
        soma+=pow(a,b);
    }
    printf("%i", soma);
    return 0;
}