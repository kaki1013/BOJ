#include <stdio.h>

int main(){
    int T, t, i, j, R;
    char S[21], ANS[161];
    
    scanf("%d", &T);
    for (t=0; t<T; t++) {
        scanf("%d %s", &R, S);

        for (i=0; i<21; i++) {
            if (S[i] == '\0') {
                ANS[R*i] = '\0';  // ���ڿ� ������� ��, strlen() �Լ�(#include <string.h>)�� ���߿� ó���ص� ��
                break;
            }
            for (j=0; j<R; j++)
                ANS[R*i+j] = S[i];
        }

        printf("%s\n", ANS);
    }

    return 0;
}