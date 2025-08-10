#include <stdio.h>
int main()
{
    int i, a, b, E, M, D, trios, restricoes=0, erros;
    scanf("%i%i%i", &E, &M, &D);
    trios = E/3;
    int duplas[M][2];
    int brigas[D][2];
    int grupos[trios][3];
    for(i=1; i<=M; i++)
    {
        scanf("%i", &duplas[i][1]);
        scanf("%i", &duplas[i][2]);
    }
    for(i=1; i<=D; i++)
    {
        scanf("%i", &brigas[i][1]);
        scanf("%i", &brigas[i][2]);
    }
    for(i=1; i<=trios; i++)
    {
        scanf("%i", &grupos[i][1]);
        scanf("%i", &grupos[i][2]);
        scanf("%i", &grupos[i][3]);
    }
    for(i=1; i<=trios; i++)
    {
        for(a=1; a<=M; a++)
        {
            if(grupos[i][1]==duplas[a][1])
            {
                if(duplas[a][2]!=grupos[i][2] && duplas[a][2]!=grupos[i][3])
                    restricoes++;
            }
            if(grupos[i][1]==duplas[a][2])
            {
                if(duplas[a][1]!=grupos[i][2] && duplas[a][1]!=grupos[i][3])
                    restricoes++;
            }
            if(grupos[i][2]==duplas[a][1])
            {
                if(duplas[a][2]!=grupos[i][1] && duplas[a][2]!=grupos[i][3])
                    restricoes++;
            }
            if(grupos[i][2]==duplas[a][2])
            {
                if(duplas[a][1]!=grupos[i][1] && duplas[a][1]!=grupos[i][3])
                    restricoes++;
            }
            if(grupos[i][3]==duplas[a][1])
            {
                if(duplas[a][2]!=grupos[i][1] && duplas[a][2]!=grupos[i][2])
                    restricoes++;
            }
            if(grupos[i][3]==duplas[a][2])
            {
                if(duplas[a][1]!=grupos[i][1] && duplas[a][1]!=grupos[i][2])
                    restricoes++;
            }
        }
        for(a=1; a<=D; a++)
        {
            if(grupos[i][1]==brigas[a][1])
            {
                if(brigas[a][2]==grupos[i][2] || brigas[a][2]==grupos[i][3])
                    restricoes++;
            }
            if(grupos[i][1]==brigas[a][2])
            {
                if(brigas[a][1]==grupos[i][2] || brigas[a][1]==grupos[i][3])
                    restricoes++;
            }
            if(grupos[i][2]==brigas[a][1])
            {
                if(brigas[a][2]==grupos[i][1] || brigas[a][2]==grupos[i][3])
                    restricoes++;
            }
            if(grupos[i][2]==brigas[a][2])
            {
                if(brigas[a][1]==grupos[i][1] || brigas[a][1]==grupos[i][3])
                    restricoes++;
            }
            if(grupos[i][3]==brigas[a][1])
            {
                if(brigas[a][2]==grupos[i][1] || brigas[a][2]==grupos[i][2])
                    restricoes++;
            }
            if(grupos[i][3]==brigas[a][2])
            {
                if(brigas[a][1]==grupos[i][1] || brigas[a][1]==grupos[i][2])
                    restricoes++;
            }
        }
    }
    printf("%i", (restricoes)/2);
    return 0;
}