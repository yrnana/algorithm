def solution(exp):
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

    return ''.join(result)


print(solution('a+b*(c^d-e)^(f+g*h)-i'))  # abcd^e-fgh*+^*+i-
