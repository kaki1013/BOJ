#include <stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);

    //정확도가 double은 12자리, float 는 6자리까지 보장합니다~ (출처: https://www.acmicpc.net/board/view/17090)
    printf("%15.13f\n",a/(double)b);
    
    return 0;
}