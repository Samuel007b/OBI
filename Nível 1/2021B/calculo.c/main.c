#include <stdio.h>
int main()
{
    int i, a, b, s, valores=0, algarismos;
    scanf("%i%i%i", &s, &a, &b);
    const int S = s;
    const int A = a;
    const int B = b;
    for(i=A; i<=B; i++)
    {
        algarismos=0;
        algarismos+=(i/10000)%10;
        algarismos+=(i/1000)%10;
        algarismos+=(i/100)%10;
        algarismos+=(i/10)%10;
        algarismos+=i%10;
        if(algarismos==S)
            valores++;
    }
    printf("%i", valores);
    return 0;
}