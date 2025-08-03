#include <stdio.h>
int main()
{
    int D, resto;
    scanf("%i", &D);
    resto = D%400;
    if(resto>200)
        printf("%i", 400-resto);
    else
        printf("%i", resto);
    return 0;
}