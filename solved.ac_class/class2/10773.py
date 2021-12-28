import sys
K = int(sys.stdin.readline().rstrip())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(K)]
stack =[]

for number in numbers:
	if number == 0:
		stack.pop()
	else:
		stack.append(number)

print(sum(stack))