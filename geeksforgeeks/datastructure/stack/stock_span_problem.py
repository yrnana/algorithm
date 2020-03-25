# 주식이 이전일로부터 몇일간 최대값이었나?
# ex) {100, 80, 60, 70, 60, 75, 85} -> {1, 1, 1, 2, 1, 4, 6}


def solution(price):
    stack = [0]

    span = [0] * len(price)
    span[0] = 1

    for i in range(1, len(price)):
        while stack and price[stack[-1]] <= price[i]:
            stack.pop()
        span[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

    return span


# print(solution([100, 80, 60, 70, 60, 75, 85]))
print(solution([10, 4, 5, 90, 120, 80]))
