#include <stdio.h>
int main()
{
    int i, j, e, m, d, restricoes=0;
    scanf("%i%i%i", &e, &m, &d);
    const int E = e;
    const int M = m;
    const int D = d;
    int trios = E/3;
    int a1[trios], a2[trios], a3[trios];
    int duplas[M][2], brigas[D][2];
    for(i=0; i<M; i++)
        scanf("%i%i", &duplas[i][0], &duplas[i][1]);
    for(i=0; i<D; i++)
        scanf("%i%i", &brigas[i][0], &brigas[i][1]);
    for(i=0; i<trios; i++)
        scanf("%i%i%i", &a1[i], &a2[i], &a3[i]);
    for(i=0; i<trios; i++)
    {
        for(j=0; j<M; j++)
        {
            if(a1[i]==duplas[j][0])
            {
                if((a2[i]!=duplas[j][1])&&(a3[i]!=duplas[j][1]))
                    restricoes++;
            }
            else if(a1[i]==duplas[j][1])
            {
                if((a2[i]!=duplas[j][0])&&(a3[i]!=duplas[j][0]))
                    restricoes++;
            }
            if(a2[i]==duplas[j][0])
            {
                if((a1[i]!=duplas[j][1])&&(a3[i]!=duplas[j][1]))
                    restricoes++;
            }
            else if(a2[i]==duplas[j][1])
            {
                if((a1[i]!=duplas[j][0])&&(a3[i]!=duplas[j][0]))
                    restricoes++;
            }
            if(a3[i]==duplas[j][0])
            {
                if((a2[i]!=duplas[j][1])&&(a1[i]!=duplas[j][1]))
                    restricoes++;
            }
            else if(a3[i]==duplas[j][1])
            {
                if((a2[i]!=duplas[j][0])&&(a1[i]!=duplas[j][0]))
                    restricoes++;
            }
        }
    }
    for(i=0; i<trios; i++)
    {
        for(j=0; j<D; j++)
        {
            if(a1[i]==brigas[j][0])
            {
                if((a2[i]==brigas[j][1])||(a3[i]==brigas[j][1]))
                    restricoes++;
            }
            else if(a1[i]==brigas[j][1])
            {
                if((a2[i]==brigas[j][0])||(a3[i]==brigas[j][0]))
                    restricoes++;
            }
            if(a2[i]==brigas[j][0])
            {
                if((a1[i]==brigas[j][1])||(a3[i]==brigas[j][1]))
                    restricoes++;
            }
            else if(a2[i]==brigas[j][1])
            {
                if((a1[i]==brigas[j][0])||(a3[i]==brigas[j][0]))
                    restricoes++;
            }
            if(a3[i]==brigas[j][0])
            {
                if((a2[i]==brigas[j][1])||(a1[i]==brigas[j][1]))
                    restricoes++;
            }
            else if(a3[i]==brigas[j][1])
            {
                if((a2[i]==brigas[j][0])||(a1[i]==brigas[j][0]))
                    restricoes++;
            }
        }
    }
    printf("%i", restricoes/2);
    return 0;
}