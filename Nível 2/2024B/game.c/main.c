#include <stdio.h>
int main()
{
    int i, N, sala=1;
    scanf("%i", &N);
    char instrucoes[N];
    for(i=1; i<=N+1; i++)
    {
        scanf("%c", &instrucoes[i]);
    }
    getchar();
    for(i=2; i<=N+1; i++)
    {
        if(instrucoes[i]=='E')
            sala*=2;
        else if(instrucoes[i]=='D')
        {
            sala*=2;
            sala+=1;
        }
    }
    printf("%i", sala);
    return 0;
}