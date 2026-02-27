#include <stdio.h>

int main()
{
    int i=0, a=0, b=0, N=0;
    scanf("%i", &N);
    char cadeia[N+1];
    getchar();
    for(i=0; i<N; i++)
    {
        scanf("%c", &cadeia[i]);
    }
    getchar();
    char cadeiaa[N+1];
    for(i=0; i<N; i++)
    {
        cadeiaa[i]=cadeia[i];
    }
    int palinImpar[N];
    for(i=0; i<N; i++)
    {
        palinImpar[i]=1;
        a=i;
        b=i;
        for(;;)
        {
            a--;
            b++;
            if(cadeia[a]==cadeia[b])
                palinImpar[i]+=2;
            else
                break;
        }
    }
    int maiorI = palinImpar[0];
    for(i=0; i<N; i++)
    {
        if(palinImpar[i]>maiorI)
            maiorI=palinImpar[i];
    }
    int palinPar[N];
    for(i=0; i<N; i++)
    {
        palinPar[i]=0;
        a=i;
        b=i+1;
        for(;;)
        {
            if(cadeiaa[a]==cadeiaa[b])
                palinPar[i]+=2;
            else
                break;
            a--;
            b++;
        }
    }
    int maiorP = palinPar[0];
    for(i=0; i<N; i++)
    {
        if(palinPar[i]>maiorP)
            maiorP=palinPar[i];
    }
    if(maiorI>maiorP)
        printf("%i", maiorI);
    else
        printf("%i", maiorP);
    return 0;
}