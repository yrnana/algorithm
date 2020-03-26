def solution(arr):
    stack = []
    for x in arr:
        if not stack:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
    return stack


print(solution(['ab', 'aa', 'aa', 'bcd', 'ab']))
