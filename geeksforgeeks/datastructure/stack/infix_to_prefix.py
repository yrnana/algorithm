def solution(exp):
    exp = list(reversed(exp))
    i = 0
    while i < len(exp):
        if exp[i] == '(':
            exp[i] = ')'
            i += 1
        elif exp[i] == ')':
            exp[i] = '('
            i += 1
        i += 1

    op = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    result, stack = [], []
    for c in exp:
        if c.isalpha():
            result.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack and stack[-1] != '(':
                return -1
            else:
                stack.pop()
        else:  # 부호
            while stack and stack[-1] in op and op[c] <= op[stack[-1]]:
                result.append(stack.pop())
            stack.append(c)
    while stack:
        result.append(stack.pop())

    return ''.join(reversed(result))


print(solution('(A+B)*(C-D)'))  # *+AB-CD
print(solution('(A-B/C)*(A/K-L)'))  # *-A/BC-/AKL
