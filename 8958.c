// 숏코딩(백준용)
// main(T,i,j,a,c){char s[80];scanf("%d",&T);for(i=0;i<T;i++){scanf("%s",s);a=0,c=0,j=0;while(s[j]!='\0'){if(s[j]=='O'){c+=1;}else{a+=(c*(c+1)/2);c=0;}j+=1;}a+=(c*(c+1)/2);printf("%d\n",a);}}
#include <stdio.h>

int main(){
    int T, i, j, ans, count;
    char s[80];
    
    scanf("%d", &T);
    for (i=0; i<T; i++) {
        scanf("%s", s);
        ans = 0, count = 0, j = 0;
        while (s[j] != '\0') {
            if (s[j] == 'O') {
                count += 1;
            }
            else {
                ans += (count * (count + 1) / 2);
                count = 0;
            }
            j += 1;
        }
        ans += (count * (count+1) / 2);  // 마지막에 ...O로 끝나는 경우
        printf("%d\n", ans);
    }

    return 0;
}