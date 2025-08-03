#include <stdio.h>
int main()
{
    int a, b, c;
    scanf("%i%i", &a, &b);
    if(a>b)
        c = 2*b-a;
    else if(b>a)
        c = 2*a-b;
    else if(a==b)
        c=a;
    printf("%i", c);
    return 0;
}
