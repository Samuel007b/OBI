#include <stdio.h>
int main()
{
    int i, x, y, a, b, n, m, k, c, l;
    char d;
    scanf("%i", &n);
    scanf("%i", &m);
    scanf("%i", &k);
    const int N=n;
    const int M=m;
    const int K=k;
    int espaco[M][N];
    for(x=0; x<M; x++)
    {
        for(y=0; y<N; y++)
        {
            espaco[x][y]=0;
        }
    }
    for(i=1; i<=K; i++)
    {
        scanf("%i", &c);
        scanf("%i", &l);
        getchar();
        scanf("%c", &d);
        if(d=='N')
        {
            for(x=l; x>=1; x--)
                espaco[x-1][c-1]=-1;
        }
        else if(d=='S')
        {
            for(x=l; x<=M; x++)
                espaco[x-1][c-1]=-1;
        }
        else if(d=='O')
        {
            for(y=c; y>=1; y--)
                espaco[l-1][y-1]=-1;
        }
        else if(d=='L')
        {
            for(y=c; y<=N; y++)
                espaco[l-1][y-1]=-1;
        }
    }
    getchar();
    if(espaco[0][0]==-1 || espaco[M-1][N-1]==-1)
        printf("N");
    else
    {
        espaco[0][0]=1;
        for(i=0; i<M*N; i++)
        {
            for(a=0; a<M; a++)
            {
                for(b=0; b<N; b++)
                {
                    if(espaco[a][b]==1)
                    {
                        if(b+1<N && espaco[a][b+1]==0)
                            espaco[a][b+1]=1;
                        if(b-1>=0 && espaco[a][b-1]==0)
                            espaco[a][b-1]=1;
                        if(a+1<N && espaco[a+1][b]==0)
                            espaco[a+1][b]=1;
                        if(a-1>=0 && espaco[a-1][b]==0)
                            espaco[a-1][b]=1;
                    }
                }
            }
        }
        if(espaco[M-1][N-1]==1)
            printf("S");
        else if(espaco[M-1][N-1]==0)
            printf("N");
    }
    return 0;
}