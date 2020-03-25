# 인쇄 대기목록의 가장 앞에 있는 문서를 대기목록에서 꺼낸다
# 나머지 인쇄 대기 목록에서 J보다 중요도가 높은 문서가 한개라도 존재하면 J를 대기목록의 마지막에 넣는다
# 그렇지 않으면 J를 인쇄


from collections import deque


def is_most_important(deq, p):
    for i, v in deq:
        if v > p:
            return False
    return True


def solution(priorities, location):
    answer = 0
    arr = [(i, v) for i, v in enumerate(priorities)]
    deq = deque(arr)

    while deq:
        j = deq.popleft()
        if is_most_important(deq, j[1]):
            answer += 1
            if j[0] == location:
                break
        else:
            deq.append(j)

    return answer


print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
