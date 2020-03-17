def solution(rule, A, B):
    if A == B:
        return rule[0]
    base = len(rule)  # 진법
    m1, m2 = dict(), dict()
    for i, r in enumerate(rule):
        m1[r] = i  # alpha -> digit
        m2[i] = r  # digit -> alpha

    a, an = 0, 1
    for i in range(len(A) - 1, -1, -1):
        a += m1[A[i]] * an
        an *= base
    b, bn = 0, 1
    for i in range(len(B) - 1, -1, -1):
        b += m1[B[i]] * bn
        bn *= base

    num = a - b
    ans = ''
    while num > 0:
        ans = m2[num % base] + ans
        num //= base
    return ans


# print(solution('zothf', 'otz', 'hh'))  # ht
# print(solution('ab', 'ba', 'a'))  # ba
print(solution('abcdefghijklmnop', 'kml', 'ba'))
