from _collections import deque


def solution(num):
    if num < 0:
        return False
    deq = deque()
    while num > 0:
        deq.appendleft(num % 10)
        num //= 10
    while len(deq) > 1:
        h = deq.popleft()
        t = deq.pop()
        if h != t:
            return False
    return True


print(solution(12345))
print(solution(-101))
print(solution(11111))
print(solution(12421))
