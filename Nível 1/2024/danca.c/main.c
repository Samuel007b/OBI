#include <stdio.h>
int main()
{
    int a, b, c, d, i, j, n, m, p, contador=0;
    scanf("%i%i%i", &n, &m, &p);
    const int N = n;
    const int M = m;
    const int P = p;
    char comandos[P];
    int fil1[P], fil2[P];
    getchar();
    for(i=0; i<P; i++)
    {
        scanf("%c", &comandos[i]);
        scanf("%i%i", &fil1[i], &fil2[i]);
        getchar();
    }
    int pista[N][M];
    for(i=0; i<N; i++)
    {
        for(j=0; j<M; j++)
        {
            contador++;
            pista[i][j] = contador;
        }
    }
    for(i=0; i<P; i++)
    {
        if(comandos[i]=='L')
        {
            for(j=0; j<M; j++)
            {
                c=fil1[i]-1;
                d=fil2[i]-1;
                a=pista[c][j];
                b=pista[d][j];
                pista[c][j] = b;
                pista[d][j] = a;
            }
        }
        else if(comandos[i]=='C')
        {
            for(j=0; j<N; j++)
            {
                c=fil1[i]-1;
                d=fil2[i]-1;
                a=pista[j][c];
                b=pista[j][d];
                pista[j][c] = b;
                pista[j][d] = a;
            }
        }
    }
    for(i=0; i<N; i++)
    {
        for(j=0; j<M; j++)
        {
            printf("%i ", pista[i][j]);
        }
        printf("\n");
    }
    return 0;
}