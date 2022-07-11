// 참고 : https://blockdmask.tistory.com/70
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> arr(201, 0);
    // -100:0, 0:100, 100:200
    int N, x, v;

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> x;
        arr[x+100] += 1;
    }
    cin >> v;
    cout << arr[v+100] << "\n";

    return 0;
}