#include <stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);

    //��Ȯ���� double�� 12�ڸ�, float �� 6�ڸ����� �����մϴ�~ (��ó: https://www.acmicpc.net/board/view/17090)
    printf("%15.13f\n",a/(double)b);
    
    return 0;
}