#include <stdio.h>
int main()
{
    int i, j, N, duplas=0, circunferencia=0;
    scanf("%i", &N);
    int arvores[N];
    getchar();
    for(i=0; i<N; i++)
    {
        scanf("%i", &arvores[i]);
        circunferencia+=arvores[i];
    }
    for(i=0; i<N; i++)
    {
        for(j=i+1; j<N; j++)
        {
            if(arvores[i]==arvores[j])
                duplas++;
        }
    }
    if(duplas>=2)
        printf("S");
    else
        printf("N");
    return 0;
}