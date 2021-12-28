# https://pannchat.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-%ED%9B%84%EC%9C%84%ED%91%9C%EA%B8%B0%EC%8B%9D-python
# 피연산자의 순서는 바뀌지 않음 / 후위 표기법은 연산자의 위치를 결정할 뿐 / 그러므로 연산자들의 순서를 스택을 통해 결정
sentence = input()
stack = []  # 피연산자가 대문자, 연산자가 소문자라면, AaBbC -> ABCba 처럼 대칭이 일어나고, 그 경계는 괄호로 구분됨
ans = ''

for char in sentence:
    # print(ans, stack)  과정 살피기 좋은 예시: A+B*(C-D)*E/F
    if char.isalpha():
        ans += char  # 피연산자라면 그대로/ 연산자들을 그 뒤에 붙임
    else:
        if char == '(':  # '(' 는 그대로 입력(구분자 역할)
            stack.append(char)
        elif char == '*' or char == '/':  # 우선순위가 상대적으로 높은 곱하기 나누기 먼저
            while stack and (stack[-1] == '*' or stack[-1] == '/'):  # A*B/C == ABC/* 처럼 우선순위가 같은 연산자 뽑아내기
                ans += stack.pop()
            stack.append(char)  # 현재 연산자는 다시 추가(중위 표기법이므로 뒤에 있는 피연산자를 쓰고, 그 뒤에 적기 위함)
        elif char == '+' or char == '-':  # 우선순위가 상대적으로 낮은 더하기 빼기는 나중에
            while stack and stack[-1] != '(':  # 이전에 담긴 연산자가 없어지거나, 괄호가 나오기 전까지
                ans += stack.pop()  # 연산자들을 빼내야 함
            stack.append(char)  # 같은 이유로, 현재 연산자는 다시 추가
        elif char == ')':  # 닫는 괄호가 나오면
            while stack and stack[-1] != '(':  # 연산자들이 남아있고, 마지막 연산자가 여는 괄호가 아닌 동안
                ans += stack.pop()  # 계속 붙여나감
            stack.pop()  # 여는 괄호 '(' 는 마지막에 제거

while stack:
    ans += stack.pop()  # 괄호와 무관하게 있던 남은 연산자들 차례로 붙여줌

print(ans)
