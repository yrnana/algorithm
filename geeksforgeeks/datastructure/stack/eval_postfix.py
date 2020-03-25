def solution(exp):
    stack = []
    for c in exp:
        if c.isdigit():
            stack.append(c)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(str(eval(val2 + c + val1)))
    return int(stack.pop())


print(solution('231*+9-'))  # 2 + 3 * 1 - 9
