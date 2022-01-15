def b_s(l, r, x):
    if l > r:
        return False
    mid = (l+r)//2
    if x < to_find[mid]:
        return b_s(l, mid-1, x)
    if x > to_find[mid]:
        return b_s(mid+1, r, x)
    return True


T = int(input())
n, A = int(input()), list(map(int, input().split()))
ASum = [0]
for i in range(n):
    ASum.append(ASum[-1] + A[i])
sub_sum_A = dict()
for i in range(n):
    for j in range(i, n):
        check = ASum[j+1] - ASum[i]
        if check in sub_sum_A:
            sub_sum_A[check] += 1
        else:
            sub_sum_A[check] = 1

m, B = int(input()), list(map(int, input().split()))
BSum = [0]
for i in range(m):
    BSum.append(BSum[-1] + B[i])
sub_sum_B = dict()
for i in range(m):
    for j in range(i, m):
        check = BSum[j+1] - BSum[i]
        if check in sub_sum_B:
            sub_sum_B[check] += 1
        else:
            sub_sum_B[check] = 1

ans = 0
to_find = sorted(sub_sum_B.keys())
l = len(to_find)
for num in sub_sum_A:
    find = T - num
    if to_find[0] <= find <= to_find[-1] and b_s(0, l-1, find):
        ans += sub_sum_A[num] * sub_sum_B[find]
print(ans)
