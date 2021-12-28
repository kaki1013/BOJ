#include <stdio.h>

int main(){
    int N, i, ans = 0;
    char a[101];

    scanf("%d", &N);
    scanf("%s", a);

    for (i=0; i<N; i++){
        ans += ((int)a[i]-48);  // '0'의 아스키 코드는 48
    }
    printf("%d", ans);

    return 0;
}