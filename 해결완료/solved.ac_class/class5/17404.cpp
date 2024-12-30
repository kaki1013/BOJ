#include <iostream>

using namespace std;

int main() {
    int N, r, g, b, ans, RGBs[1000][3], dp[1000][3];
    
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> r >> g >> b;
        RGBs[i][0] = r;
        RGBs[i][1] = g;
        RGBs[i][2] = b;
    }
    
    ans = 1000001;
    for (int last_color = 0; last_color < 3; last_color++) {
        for (int init_color = 0; init_color < 3; init_color++)
            dp[0][init_color] = (init_color == last_color) ? 1001 : RGBs[0][init_color];
        for (int i = 0; i < N-1; i++) {
            dp[i+1][0] = min(dp[i][1], dp[i][2]) + RGBs[i+1][0];
            dp[i+1][1] = min(dp[i][0], dp[i][2]) + RGBs[i+1][1];
            dp[i+1][2] = min(dp[i][0], dp[i][1]) + RGBs[i+1][2];
        }
        ans = min(ans, dp[N-1][last_color]);
    }

    cout << ans << "\n";

    return 0;
}
