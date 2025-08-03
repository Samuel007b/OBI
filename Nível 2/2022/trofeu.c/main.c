#include <stdio.h>
int main()
{
    int a=0, i, q, trofeu=0, placa=0;
    int P[6];
    for(i=1; i<=5; i++)
    {
        scanf("%i", &P[i]);
    }
    int maior=P[1];
    for(i=1; i<=5; i++)
    {
        if(P[i]>maior)
            maior=P[i];
    }
    for(i=1; i<=5; i++)
    {
        if(P[i]==maior)
            trofeu++;
    }
    q=5-trofeu;
    int Q[q+1];
    for(i=1; i<=5; i++)
    {
        if(P[i]!=maior)
        {
            a++;
            Q[a]=P[i];
        }
    }
    int medio=Q[1];
    for(i=1; i<=q; i++)
    {
        if(Q[i]>medio)
            medio=Q[i];
    }
    for(i=1; i<=q; i++)
    {
        if(Q[i]==medio)
            placa++;
    }
    printf("%i %i", trofeu, placa);
    return 0;
}