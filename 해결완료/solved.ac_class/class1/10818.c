#include <stdio.h>

int main(){
    int N, i, x, M, m;
    scanf("%d", &N);
    scanf("%d", &x);
    M = x, m = x;
    
    for (i=1;i<N;i++) {
        scanf("%d", &x);
        if (x>M)
            M = x;
        if (x<m)
            m = x;
    }
    
    printf("%d %d", m, M);

    return 0;
}