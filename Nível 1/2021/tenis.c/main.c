#include <stdio.h>
int main()
{
    int A, B, C, D, melhor, pior, diferenca;
    scanf("%i%i%i%i", &A, &B, &C, &D);
    melhor=A;
    if(B>melhor)
        melhor=B;
    if(C>melhor)
        melhor=C;
    if(D>melhor)
        melhor=D;
    pior=A;
    if(B<pior)
        pior=B;
    if(C<pior)
        pior=C;
    if(D<pior)
        pior=D;
    diferenca = (A+B+C+D)-2*(melhor+pior);
    if(diferenca<0)
        diferenca*=-1;
    printf("%i", diferenca);
    return 0;
}