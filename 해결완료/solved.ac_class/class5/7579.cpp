#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, M, x, now_m, now_c, ans;
    int m[101], c[101];
    int dp[101][10001] = {0,};

    // INPUT
    cin >> N >> M;
    for (int i=1; i<=N; i++) cin >> m[i];
    for (int i=1; i<=N; i++) cin >> c[i];

    // dp[app][cost] := 1번부터 app번까지의 앱을 사용하여 cost까지의 비용을 허락하면, 확보할 수 있는 최대 메모리
    for (int app=1; app<=N; app++) {
        now_m = m[app]; now_c = c[app];
        dp[app][now_c] = max(dp[app-1][now_c], now_m);  // app번째 앱까지 사용하지 않는 최대 메모리는, app-1번째 앱까지 사용했을 때 혹은 app번째 앱 하나만 사용 
        for (int cost=0; cost<10001; cost++) {
            if (cost < now_c) dp[app][cost] = dp[app-1][cost];  // now_c보다 작으면, 이전 앱까지 사용한 dp 값과 동일
            else dp[app][cost] = max(dp[app-1][cost], dp[app-1][cost-now_c]+now_m);  // 그렇지 않으면, 이전 앱까지 사용한 dp 값 혹은 이번 앱까지 사용한 값 중 최대 값
        }
    }

    // ans..
    for (int cost=0; cost<10001; cost++) {
        if (dp[N][cost] >= M) {
            ans = cost;
            break;
        }
    }
    cout << ans;
    return 0;
}

// 예제 dp 출력
// 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
// 0 0 0 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30
// 10 10 10 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40
// 10 10 10 40 40 40 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60
// 10 10 10 40 40 45 60 60 75 75 75 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95
// 10 10 10 40 50 50 60 80 80 85 100 100 115 115 115 135 135 135 135 135 135 135 135 135 135 135 135 135 135 135
