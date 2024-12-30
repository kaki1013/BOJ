// cin과 getline을 같이 사용할때 cin.ignore()이 필요한 이유 기록
// https://namwhis.tistory.com/entry/cin%EA%B3%BC-getline%EC%9D%84-%EA%B0%99%EC%9D%B4-%EC%82%AC%EC%9A%A9%ED%95%A0%EB%95%8C-cinignore%EC%9D%B4-%ED%95%84%EC%9A%94%ED%95%9C-%EC%9D%B4%EC%9C%A0-%EA%B8%B0%EB%A1%9D
#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    string word;
    
    cin >> T;
    cin.ignore();
    for (int i=0; i<T; i++) {
        getline(cin, word);
        cout << word[0] << word[word.length() - 1] <<"\n";
    }
    
    return 0;
}