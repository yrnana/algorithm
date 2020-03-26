def solution(n, times):
    left, right = 0, max(times) * n
    orig_right = right
    answer = right
    while right >= left:
        p = 0
        mid = (left + right) // 2  # 이분탐색으로 가정한 총 시간
        for t in times:
            p += mid // t  # n = ans // t1 + ans // t2 + ...
        if p == n:
            answer = min(answer, mid)
            right = mid - 1  # 총 시간을 줄여서 또 해당값이 있는지 검색
        elif p > n:
            right = mid - 1
        else:  # p < n
            left = mid + 1
    return right + 1 if answer == orig_right else answer


# print(solution(6, [7, 10]))  # 28
# print(solution(6, [3, 4, 7]))  # 9
print(solution(7, [3, 4, 7]))  # 12
