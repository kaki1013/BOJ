#include <stdio.h>
#define SIZE_N 100
#define SIZE_K 10000
#define INF 100000

int main()
{
    int n, k, now;
    int coins[SIZE_N], dp[SIZE_K];

    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++)
        scanf("%d", &coins[i]);

    for (int i = 0; i < k+1; i++)
        dp[i] = INF;
    dp[0] = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < k+1; j++)
        {
            now = coins[i];
            if (j >= now)
                dp[j] = (dp[j] < dp[j-now] + 1) ? dp[j] : dp[j-now] + 1;
        }        
    }
    printf("%d\n", (dp[k] == INF) ? -1 : dp[k]);    
}