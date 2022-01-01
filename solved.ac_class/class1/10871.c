#include <stdio.h>

#define SIZE 10000

int main() {
    int N, X, A;

    scanf("%d %d", &N, &X);
    for (int i = 0; i < N; i++) {
        scanf("%d", &A);
        if (A < X)
            printf("%d ", A);
    }
    
    return 0;
}