#include <stdio.h>

int main(){
    int T, t, i, j, R;
    char S[21], ANS[161];
    
    scanf("%d", &T);
    for (t=0; t<T; t++) {
        scanf("%d %s", &R, S);

        for (i=0; i<21; i++) {
            if (S[i] == '\0') {
                ANS[R*i] = '\0';  // 문자열 끝내줘야 함, strlen() 함수(#include <string.h>)로 나중에 처리해도 됨
                break;
            }
            for (j=0; j<R; j++)
                ANS[R*i+j] = S[i];
        }

        printf("%s\n", ANS);
    }

    return 0;
}