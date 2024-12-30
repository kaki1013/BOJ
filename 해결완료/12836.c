#include <stdio.h>
#include <stdlib.h>

int main(){
    int N, Q, cmd, x, y;
    long long int *days, ans;

    scanf("%d %d", &N, &Q);
    days = (long long int *)malloc((N+1)*sizeof(long long int));
    for (int i = 0; i <= N; i++)
        days[i] = 0;

    for (int i = 0; i < Q; i++){
        scanf("%d %d %d", &cmd, &x, &y);
        if (cmd == 1)
            days[x] += y;
        else{
            ans = 0;
            for (int day = x; day <= y; day++)
                ans += days[day];
            printf("%lld\n", ans);
        }
    }

    return 0;
}