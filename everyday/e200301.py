# https://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/
# 정렬된 양수(positive integer) 배열이 주어지면, 배열 원소들의 합으로 만들수 없는 가장 작은 양수를 구하시오.


def solution(arr):
    ans = 1
    for x in arr:
        if x <= ans:
            ans += x
        else:
            break
    return ans


print(solution([1, 2, 3, 8]))
