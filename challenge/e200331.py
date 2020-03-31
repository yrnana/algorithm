def solution(distance, rocks, n):
    # 최소거리에 대한 제거해야 할 바위 수를 구한다
    # 많이 제거할수록 최소거리가 증가
    ans = 0
    rocks.sort()
    left, right = 0, distance
    while left <= right:
        d = (left + right) // 2  # 최소거리로 가정
        prev, remove = 0, 0
        for rock in rocks:
            if rock - prev < d:
                remove += 1  # 바위 사이의 갭이 최소거리보다 작다면 바위 제거
            else:
                prev = rock  # 갭이 더 크면 바위를 제거하지 않고 이전 바위로 저장
        if remove > n:
            # 더 많이 제거했다면 거리를 좁혀야 한다
            right = d - 1
        else:
            # 덜 제거했다면 거리를 늘려야 한다
            left = d + 1
            ans = d
    return ans


print(solution(25, [2, 14, 11, 21, 17], 2))  # 4
