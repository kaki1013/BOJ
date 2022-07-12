/*
https://blog.naver.com/isaac7263/221633998534
c++에서 c언어의 표준함수 호출하기
*/
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M, x;
    vector<vector<int>> matrix;
    vector<int> v;
    
    scanf("%d %d", &N, &M);

    for (int i=0; i<N; i++) {
        v.clear();
        for (int j=0; j<M; j++) {
            scanf("%d", &x);
            v.push_back(x);
        }
        matrix.push_back(v);
    }

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            scanf("%d", &x);
            matrix[i][j] += x;
        }
    }
    
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++)
            printf("%d ", matrix[i][j]);
        printf("\n");
    }

    return 0;
}