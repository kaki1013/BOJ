// https://donggod.tistory.com/55
// scanf�� ���������� �޾ƿ� ���� return, ���� ������ �߻��ϰų� EOF(End of File)�� ������ -1�� return
// EOF�� �ֿܼ��� ctrl + z �� �Է� ����
#include <stdio.h>

int main(){
    int A, B;

    while (scanf("%d %d", &A, &B) != EOF)  // EOF = -1 = 111..1 �̹Ƿ� ~EOF = 000..0 �� �̿��Ͽ� �������� ��� ����
        printf("%d\n", A+B);
    
    return 0;
}