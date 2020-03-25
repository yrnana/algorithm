def solution(exp):
    stack = []
    for c in exp[::-1]:
        if c.isalpha():
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + c)
    return stack[-1]


print(solution('*+AB-CD'))  # AB+CD-*
print(solution('*-A/BC-/AKL'))  # ABC/-AK/L-*
