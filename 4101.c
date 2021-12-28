/*
0 0 일 때 출력이 있음
#include <stdio.h>

int main(){
    long x, y;
    
    do
    {
        scanf("%d %d", &x, &y);
        if (x>y)
            printf("Yes\n");
        else
            printf("No\n");
    } while ((x != 0) | (y != 0));
    
    return 0;
}
*/
#include <stdio.h>

int main(){
    long x, y;
    
    while (0 == 0)
    {
        scanf("%d %d", &x, &y);

        if ((x == 0) & (y == 0))
            break;
        else if (x>y)
            printf("Yes\n");
        else
            printf("No\n");
    }
    
    return 0;
}