#include <stdio.h>
int main()
{
    int i, N;
    scanf("%i", &N);
    char caracteres[N+1];
    int contador[N+1];
    for(i=1; i<=N+1; i++)
    {
        scanf("%c", &caracteres[i]);
        contador[i]=1;
    }
    for(i=2; i<=N+1; i++)
    {
        if(caracteres[i]==caracteres[i+1])
        {
            contador[i]++;
            contador[i+1]=contador[i];
        }
        else
            printf("%i %c ", contador[i], caracteres[i]);
    }
    return 0;
}
