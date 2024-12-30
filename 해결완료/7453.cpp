#include <bits/stdc++.h>

using namespace std;

int main(int argc, char** argv) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    int A[N], B[N], C[N], D[N];
    int s1[N*N], s2[N*N];

    for (int i=0; i<N; i++) {
        cin >> A[i];
        cin >> B[i];
        cin >> C[i];
        cin >> D[i];
    }
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            s1[i*N+j] = A[i] + B[j];
            s2[i*N+j] = C[i] + D[j];
        }
    }

    sort(s1, s1+N*N);
    sort(s2, s2+N*N);

    long long ans = 0;
    int tmp, l, r;
    for (int i = 0; i < N * N; i++) {
        tmp = s1[i];
        l = lower_bound(s2, s2 + N*N, -tmp) - s2;
        r = upper_bound(s2, s2 + N*N, -tmp) - s2;

        if (s2[l] == -tmp) {
            ans += r-l;
        }
    }

    cout << ans << '\n';

	return 0;
}