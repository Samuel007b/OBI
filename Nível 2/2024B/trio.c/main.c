#include <stdio.h>
int main()
{
    int i, a, b, c, N, trios=0;
    scanf("%i", &N);
    int palitos[N];
    for(i=1; i<=N; i++)
    {
        scanf("%i", &palitos[i]);
    }
    for(a=1; a<=N; a++)
    {
        for(b=a+1; b<=N; b++)
        {
            for(c=b+1; c<=N; c++)
            {
                if(palitos[a]<(palitos[b]+palitos[c]))
                {
                    if(palitos[b]<(palitos[a]+palitos[c]))
                    {
                        if(palitos[c]<(palitos[a]+palitos[b]))
                            trios++;
                    }
                }
            }
        }
    }
    printf("%i", trios);
    return 0;
}