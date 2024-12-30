n = int(input())
s = 0
count = -1
while (n+2) // (4**s):
    k = (n+2) // (4**s)
    k = (k+1) // 2
    count += k
    s += 1
print(count)

# short-1
n,s,c=int(input())+2,1,-1
while n//s:c+=(n//s+1)//2;s*=4
print(c)

# short-final, 참고: https://www.acmicpc.net/source/33826540
n,c=int(input())+2,-1
while n:c+=(n+1)//2;n//=4
print(c)