#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    vector<int> arr(30);
    
    for (int i=0; i<28; i++) {
        cin >> n;
        arr[n-1] = 1;
    }

    for (int i=0; i<30; i++) {
        if (arr[i] == 1) continue;
        cout << i+1 << "\n";
    }

    return 0;
}