#include <iostream>

using namespace std;

int main() {
    long long N, M, ans;
    cin >> N >> M;
    ans = (N>M) ? N-M : M-N;
    cout << ans << "\n";
}