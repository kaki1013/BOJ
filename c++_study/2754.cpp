#include <iostream>
#include <string>

using namespace std;

int main() {
    string score, num;

    getline(cin, score);
    if (score == "A+") num = "4.3";
    else if (score == "A0") num = "4.0";
    else if (score == "A-") num = "3.7";
    else if (score == "B+") num = "3.3";
    else if (score == "B0") num = "3.0";
    else if (score == "B-") num = "2.7";
    else if (score == "C+") num = "2.3";
    else if (score == "C0") num = "2.0";
    else if (score == "C-") num = "1.7";
    else if (score == "D+") num = "1.3";
    else if (score == "D0") num = "1.0";
    else if (score == "D-") num = "0.7";
    else num = "0.0";

    cout << num << "\n";

    return 0;
}