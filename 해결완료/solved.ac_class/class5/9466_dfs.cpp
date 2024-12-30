#include <iostream>
#include <cstring>  // to use memset()
#define SIZE 100001
using namespace std;

int length, succ[SIZE];
bool vst[SIZE], InStack[SIZE];

void dfs(int s) {
    if (vst[s]) return;
    vst[s] = InStack[s] = true;
    int nxt = succ[s];
    if (InStack[nxt]) {
        length++;
        if (nxt != s) for (int node = nxt; node != s; node = succ[node]) length++;
    }
    else dfs(nxt);
    InStack[s] = false;
    return;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        for (int i=1; i<=n; i++) cin >> succ[i];
        memset(vst, false, sizeof(bool)*(n+1));
        length = 0;
        for (int i=1; i<=n; i++) dfs(i);
        cout << n - length << "\n";
    }
    return 0;
}
