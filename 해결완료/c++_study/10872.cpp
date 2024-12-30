#include <stdio.h>

int main() {
    int N, ans = 1;
    scanf("%d", &N);
    for (int i = 1; i <= N; i++)
        ans *= i;
    printf("%d", ans);
}

// sol2
#include <iostream>

using namespace std;

int main() {
    int N, ans;
    cin >> N;
    for (int i = 1; i <= N; i++)
        ans *= i;
    cout << ans << "\n";
}