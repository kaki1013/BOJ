#include <stdio.h>

int main(){
    int T, i, A, B;
    
    scanf("%d", &T);
    for (i=1; i<=T; i++) {
        scanf("%d,%d", &A, &B);
        printf("%d\n",A+B);

    }
    
    return 0;
}