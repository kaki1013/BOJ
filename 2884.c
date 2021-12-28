#include <stdio.h>

int main(){
    int H, M;
    
    scanf("%d %d", &H, &M);
    if (M >= 45)
        printf("%d %d", H, M-45);
    else
        printf("%d %d", ((H-1)+24)%24, M+15);
    return 0;
}