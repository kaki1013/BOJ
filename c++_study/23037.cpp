#include <iostream>
#include <cmath>

using namespace std;

int five(int n);

int main() {
    int n;

    cin >> n;
    cout << five(n) << "\n";

    return 0;
}

int five(int n) {
    if (n < 10) return pow(n, 5);
    else return five(n/10) + pow(n%10, 5);
}