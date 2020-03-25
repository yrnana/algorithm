def solution(exp):
    stack = []
    for c in exp:
        if c.isalpha():
            stack.insert(0, c)
        else:
            op1 = stack.pop(0)
            op2 = stack.pop(0)
            stack.insert(0, '(' + op2 + c + op1 + ')')
    return stack[0][1:-1]


print(solution('abc++'))  # (a + (b + c))
print(solution('abcd^e-fgh*+^*+i-'))  # a+b*(c^d-e)^(f+g*h)-i
