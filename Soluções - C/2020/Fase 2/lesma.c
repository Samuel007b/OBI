#include <stdio.h>
int main()
{
    int A, S, D, trajeto=0, dias=0;
    scanf("%i%i%i", &A, &S, &D);
    for(;;)
    {
        dias++;
        trajeto+=S;
        if(trajeto>=A)
            break;
        else
            trajeto-=D;
    }
    printf("%i", dias);
    return 0;
}