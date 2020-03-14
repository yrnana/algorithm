# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

from collections import deque


def is_most_important(j, deq):
    for x in deq:
        if x[1] > j[1]:
            return False
    return True


def solution(priorities, location):
    answer = 1
    # (인덱스, 우선순위) : (idx, priority)
    deq = deque([(i, v) for i, v in enumerate(priorities)])
    while deq:
        j = deq.popleft()
        if is_most_important(j, deq):
            # 인쇄
            if location == j[0]:
                return answer
            answer += 1
        else:
            deq.append(j)
    return answer


print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
