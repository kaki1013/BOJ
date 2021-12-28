#include <stdio.h>

int main(){
    int i, n;
    int Max = 0, idx = 0;

    for (i = 1; i <= 9; i++) {
        scanf("%d", &n);
        if (n > Max) {
            Max = n;
            idx = i;
        }
    }
    printf("%d\n%d", Max, idx);

    return 0;
}