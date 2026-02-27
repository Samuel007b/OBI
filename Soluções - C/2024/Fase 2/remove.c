#include <stdio.h>
int main()
{
    int i, N, passos=0, cent_milhar, dez_milhar, uni_milhar, centena, dezena, unidade, maior;
    scanf("%i", &N);
    for(;;)
    {
        cent_milhar=N/100000;
        dez_milhar=(N/10000)-(10*cent_milhar);
        uni_milhar=(N/1000)-(100*cent_milhar)-(10*dez_milhar);
        centena=(N/100)-(1000*cent_milhar)-(100*dez_milhar)-(10*uni_milhar);
        dezena=(N/10)-(10000*cent_milhar)-(1000*dez_milhar)-(100*uni_milhar)-(10*centena);
        unidade=N%10;
        maior=cent_milhar;
        if(dez_milhar>maior)
            maior=dez_milhar;
        if(uni_milhar>maior)
            maior=uni_milhar;
        if(centena>maior)
            maior=centena;
        if(dezena>maior)
            maior=dezena;
        if(unidade>maior)
            maior=unidade;
        N=N-maior;
        passos++;
        if(N==0)
            break;
    }
    printf("%i", passos);
    return 0;
}