#include <stdio.h>
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
int main(){
    int x, y, w, h, ans;
    scanf("%d %d %d %d", &x, &y, &w, &h);
    ans = MIN(MIN(x, y), MIN(w-x, h-y));
    printf("%d\n", ans);
}