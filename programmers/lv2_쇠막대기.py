def solution(arrangement):
    answer = 0
    stack = []
    for token in arrangement:
        if token == '(':
            stack.append(token)
            last = token
        else:
            stack.pop()
            if last == '(':  # 레이저인경우
                answer += len(stack)
                last = token
            else:
                answer += 1
    return answer


print(solution('()(((()())(())()))(())'))
