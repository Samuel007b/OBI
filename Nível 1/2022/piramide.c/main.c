#include <stdio.h>
int main()
{
    int a, i, j, n, topo;
    scanf("%d", &n);
    const int N = n;
    int piramide[N][N];
    if(N%2==0)
        topo=N/2;
    else
        topo=(N+1)/2;
    for(a=topo; a>0; a--)
    {
        for(i=0; i<N; i++)
        {
            for(j=0; j<N; j++)
            {
                if(i==a-1 || j==a-1)
                    piramide[i][j]=a;
                else if(i==N-a || j==N-a)
                    piramide[i][j]=a;
            }
        }
    }
    for(i=0; i<N; i++)
    {
        for(j=0; j<N; j++)
        {
            printf("%i ", piramide[i][j]);
        }
        printf("\n");
    }
    return 0;
}