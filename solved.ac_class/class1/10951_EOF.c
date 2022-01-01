// https://donggod.tistory.com/55
// scanf는 성공적으로 받아온 수를 return, 만약 에러가 발생하거나 EOF(End of File)를 만나면 -1을 return
// EOF는 콘솔에서 ctrl + z 로 입력 가능
#include <stdio.h>

int main(){
    int A, B;

    while (scanf("%d %d", &A, &B) != EOF)  // EOF = -1 = 111..1 이므로 ~EOF = 000..0 을 이용하여 조건으로 사용 가능
        printf("%d\n", A+B);
    
    return 0;
}