#include <stdio.h>
int main()
{
    float combustivel, C, D, T;
    scanf("%f%f%f", &C, &D, &T);
    combustivel = (D/C)-T;
    if(combustivel>=0)
        printf("%.1f", combustivel);
    else
        printf("0.0");
    return 0;
}