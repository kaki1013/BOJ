/*
1. #include <bits/stdc++.h>
bits/stdc++.h 헤더는 모든 표준 라이브러리가 포함된 헤더
 
장점
- 프로그래밍 대회에서 쓸데없는 시간낭비를 줄여주므로 사용하면 좋습니다.
- 필요한 헤더 파일 include 구문을 작성하는데 시간을 줄여줍니다.
- STL이나 GNU C++의 모든 함수들을 기억할 필요가 없습니다.

단점
- bits/stdc++.h 헤더는 GNU C++ 라이브러리의 표준 헤더가 아니기 때문에, GCC가 아닌 다른 컴파일러로 빌드를 하려고 한다면 실패합니다.
- 쓸대없는 파일들을 추가시켜서 컴파일 시간이 늘어납니다.
- 표준 C++이 아니기 때문에 이식성이 있지도 않고, 컴파일러 종속적입니다.
출처 : https://eine.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%9E%AC-%ED%92%80-%EB%95%8C-%EC%9C%A0%EC%9A%A9%ED%95%9C-C%EC%97%90%EC%84%9C-bitsstdch-%ED%97%A4%EB%8D%94%ED%8C%8C%EC%9D%BC

===============================================================

눈치 챈 사람들도 있겠지만 bits/stdc++.h라는 이름은 경로의 이름이다.
다시 말하면 bits라는 폴더 안에 stdc++.h라는 이름을 가진 헤더 파일을 include 한다는 뜻이다.
출처 : https://miniolife.tistory.com/11

===============================================================

자주쓰는 헤더? : algorithm, stack, vector 

===============================================================

2. using namespace std;

의미: std 클래스에 정의되어 있는 함수들을 사용하겠다!
출처 : https://blog.naver.com/unicone/60063769910

using namespace std를 사용하면 안되는 이유
출처 : https://sexycoder.tistory.com/16

===============================================================

3. 풀만한 문제들
https://www.acmicpc.net/problem/2557
https://www.acmicpc.net/problem/11382
https://www.acmicpc.net/problem/10872
https://www.acmicpc.net/problem/15552

4. 빠른 입출력
ios::sync_with_stdio(0);
cin.tie(0);
===============================================================

C++의 cout cin가 scanf 나 printf 에 비해서 느리기 때문에 가속화 시킬 목적   // 출처: https://doomed-lab.tistory.com/54

===============================================================

scanf/prinf는 충분히 빠름.
endl = 개행문자를 출력 + 출력 버퍼를 비우는 역할 => 버퍼를 비우는 작업이 매우 느림 & 온라인 저지에서는 무엇이 출력되는가가 중요 => endl을 '\n'으로 바꾸기
cin.tie(NULL)은 cin과 cout의 묶음을 풀어 줍니다. 기본적으로 cin으로 읽을 때 먼저 출력 버퍼를 비우는데, 마찬가지로 온라인 저지에서는 화면에 바로 보여지는 것이 중요하지 않습니다. 입력과 출력을 여러 번 번갈아서 반복해야 하는 경우 필수적입니다.
ios_base::sync_with_stdio(false)는 C와 C++의 버퍼를 분리합니다. 이것을 사용하면 cin/cout이 더 이상 stdin/stdout과 맞춰 줄 필요가 없으므로 속도가 빨라집니다. 단, 버퍼가 분리되었으므로 cin과 scanf, gets, getchar 등을 같이 사용하면 안 되고, cout과 printf, puts, putchar 등을 같이 사용하면 안 됩니다.
출처 : https://www.acmicpc.net/board/view/22716

===============================================================
cin, cout과 scanf, printf 차이점 (11659번 : 구간 합 구하기 4)
참고: https://restudycafe.tistory.com/m/354


*/

// 기본 템플릿
#include <iostream>

using namespace std;

int main() {
    // 풀이 작성
    int a, b;
    cin >> a >> b;
    cout << a+b << "\n";
}
