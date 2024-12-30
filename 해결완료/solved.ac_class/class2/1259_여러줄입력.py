import sys
while True:
    s = sys.stdin.readline().rstrip()  # strip 없으면 \n 존재
    if s == '0':
        break
    if s == s[::-1]:
        print('yes')
    else:
        print('no')