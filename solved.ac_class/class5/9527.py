def bit_sum(n):
    # from 0 to n
    count = 0
    s = 1
    while (n + 1) // s:
        count += ((n + 1) // (2 * s)) * s
        temp = (n + 1) % (2 * s)
        count += 0 if temp <= s else temp % s
        s *= 2
    return count


A, B = map(int, input().split())
print(bit_sum(B) - bit_sum(A - 1))


# short
def S(n):
    c,s=0,1;n+=1
    while n//s:c+=n//(2*s)*s+max(0,n%(2*s)-s);s*=2
    return c
A,B=map(int,input().split())
print(S(B)-S(A-1))