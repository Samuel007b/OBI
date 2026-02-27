#include <stdio.h>
int main()
{
    int a=0, i, j, l, c;
    scanf("%i%i", &l, &c);
    const int L = l;
    const int C = c;
    char variavel[C*L][3];
    int Sx[L], Sy[C];
    getchar();
    for(i=0; i<L; i++)
    {
        for(j=0; j<C; j++)
        {
            scanf("%s", variavel[a]);
            a++;
            getchar();
        }
        scanf("%i", &Sx[i]);
    }
    for(i=0; i<C; i++)
    {
        scanf("%i", &Sy[i]);
    }
    
    

    return 0;
}