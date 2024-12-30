#include <stdio.h>

int main()
{
    int x, y, ans;
    scanf("%d %d", &x, &y);
    ans = (x>0) ? ((y>0) ? 1 : 4) : ((y>0) ? 2 : 3);
    printf("%d\n", ans);
}