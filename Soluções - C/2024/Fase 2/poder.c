#include <stdio.h>

int main()
{
    int i, j, N, M, linhas, colunas, maior;
    scanf("%i%i", &N, &M);
    linhas = N;
    colunas = M;
    int matriz[linhas][colunas];
    int poder1[linhas][colunas];
    int poder2[linhas][colunas];
    for(i=1; i<=linhas; i++)
    {
        for(j=1; j<=colunas; j++)
        {
            scanf("%i", &matriz[i][j]);
            poder1[i][j]=matriz[i][j];
        }
    }
    for(i=1; i<=linhas; i++)
    {
        for(j=1; j<=colunas; j++)
        {
            maior=matriz[i][j+1];
            if(maior<matriz[i][j-1])
                maior=matriz[i][j-1];
            if(maior<matriz[i+1][j])
                maior=matriz[i+1][j];
            if(maior<matriz[i-1][j])
                maior=matriz[i-1][j];
            if(matriz[i][j]>=maior)
            {
                poder1[i][j]+=matriz[i][j+1];
                poder1[i][j]+=matriz[i][j-1];
                poder1[i][j]+=matriz[i+1][j];
                poder1[i][j]+=matriz[i-1][j];
            }
            else if()
            {
                
            }
            if(matriz[i][j]>=matriz[i][j+1])
                poder1[i][j]+=matriz[i][j+1];
            if(matriz[i][j]>=matriz[i][j-1])
                poder1[i][j]+=matriz[i][j-1];
            if(matriz[i][j]>=matriz[i+1][j])
                poder1[i][j]+=matriz[i+1][j];
            if(matriz[i][j]>=matriz[i-1][j])
                poder1[i][j]+=matriz[i-1][j];
            
            poder2[i][j]=poder1[i][j];
        }
    }
    for(i=1; i<=linhas; i++)
    {
        for(j=1; j<=colunas; j++)
        {
            for(;;)
            {
                if(poder1[i][j]>=poder1[i][j+1])
                    poder2[i][j]+=(poder1[i][j+1]-matriz[i][j+1]);
                if(poder1[i][j]>=poder1[i][j-1])
                    poder2[i][j]+=(poder1[i][j-1]-matriz[i][j-1]);
                if(poder1[i][j]>=poder1[i+1][j])
                    poder2[i][j]+=(poder1[i+1][j]-matriz[i+1][j]);
                if(poder1[i][j]>=poder1[i-1][j])
                    poder2[i][j]+=(poder1[i-1][j]-matriz[i-1][j]);
                else
                    break;
            }
        }
    }
    
    for(i=1; i<=linhas; i++)
    {
        for(j=1; j<=colunas; j++)
        {
            printf("%i ", poder[i][j]);
        }
        printf("\n");
    }
    return 0;
}