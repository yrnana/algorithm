# 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.
# 예를 들어 집합 A = {1, 2, 3}, 집합 B = {2, 3, 4}라고 할 때,
# 교집합 A ∩ B = {2, 3}, 합집합 A ∪ B = {1, 2, 3, 4}이 되므로, 집합 A, B 사이의 자카드 유사도 J(A, B) = 2/4 = 0.5가 된다.
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.

from math import floor


def intersection(arr1, arr2):
    res = []
    l1, l2 = len(arr1), len(arr2)
    i1, i2 = 0, 0
    while i1 < l1 and i2 < l2:
        if arr1[i1] < arr2[i2]:
            i1 += 1
        elif arr1[i1] > arr2[i2]:
            i2 += 1
        else:
            res.append(arr2[i2])
            i1 += 1
            i2 += 1
    return res


def union(arr1, arr2):
    res = []
    l1, l2 = len(arr1), len(arr2)
    i1, i2 = 0, 0
    while i1 < l1 and i2 < l2:
        if arr1[i1] < arr2[i2]:
            res.append(arr1[i1])
            i1 += 1
        elif arr1[i1] > arr2[i2]:
            res.append(arr2[i2])
            i2 += 1
        else:
            res.append(arr2[i2])
            i1 += 1
            i2 += 1
    while i1 < l1:
        res.append(arr1[i1])
        i1 += 1
    while i2 < l2:
        res.append(arr2[i2])
        i2 += 1
    return res


def solution(str1, str2):
    s1, s2 = [], []
    for i in range(len(str1) - 1):
        s = str1[i] + str1[i + 1]
        if s.isalpha():
            s1.append(s.upper())
    for i in range(len(str2) - 1):
        s = str2[i] + str2[i + 1]
        if s.isalpha():
            s2.append(s.upper())
    s1.sort()
    s2.sort()

    u = len(union(s1, s2))
    if u == 0:
        return 1 * 65536
    i = len(intersection(s1, s2))
    return floor((i / u) * 65536)


print(solution('FRANCE', 'french'))  # 16384
print(solution('handshake', 'shake hands'))  # 65536
print(solution('aa1+aa2', 'AAAA12'))  # 43690
print(solution('E=M*C^2', 'e=m*c^2'))  # 65536
