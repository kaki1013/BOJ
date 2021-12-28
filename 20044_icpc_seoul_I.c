// Seoul Nationalwide Internet Competition 2020 I
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a , const void *b) {
    if( *(int*)a > *(int*)b ) return 1;
    else if( *(int*)a < *(int*)b ) return -1;
    else return 0;
} 

int main() {
    int n, ans;
    int w[10000];

    scanf("%d", &n);
    for (int i=0;i<2*n;i++)
        scanf("%d", &w[i]);

    qsort(w, 2*n, sizeof(w[0]), compare);
    ans = w[0] + w[2*n-1];
    for (int i=1; i<n; i++) {
        if (w[i] + w[2*n-1-i] < ans) {
            ans = w[i] + w[2*n-1-i];
        }
    }

    printf("%d\n", ans);
}