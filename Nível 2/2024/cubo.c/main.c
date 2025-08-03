#include <stdio.h>
#include <math.h>
int main()
{
    int N, uma, duas, tres, nenhuma;
    scanf("%i", &N);
    nenhuma = pow((N-2),3);
    uma = pow((N-2),2)*6;
    tres = 8;
    duas = (pow((N),3))-nenhuma-uma-tres;
    printf("%i\n%i\n%i\n%i", nenhuma, uma, duas, tres);
    return 0;
}