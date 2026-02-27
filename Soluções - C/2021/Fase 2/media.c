#include <stdio.h>
int main()
{
    int A, B, C;
    scanf("%i%i", &A, &B);
    if(A>B)
        C=2*B-A;
    else if(A<B)
        C=2*A-B;
    else if(A==B)
        C=A;
    printf("%i", C);
    return 0;
}