#include <stdio.h>
int main()
{
    int R, M, L;
    scanf("%i%i%i", &R, &M, &L);
    if(R<M)
        printf("RM\n");
    else
        printf("*\n");
    if(R<L)
        printf("RO");
    else
        printf("*");
    return 0;
}