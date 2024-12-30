#include <iostream>
#include <string>

using namespace std;

int main() {
    string word;

    getline(cin, word);
    for (int i=0; i<word.length(); i++) {
        if ('a' <= word[i] && word[i] <= 'z') word[i] += -'a' + 'A';
        else word[i] += -'A' + 'a';
    }
    cout << word << "\n";
    return 0;
}