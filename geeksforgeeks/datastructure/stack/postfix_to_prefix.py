def solution(exp):
    stack = []
    for c in exp:
        if c.isalpha():
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(c + op2 + op1)
    return stack[-1]


print(solution('AB+CD-*'))  # *+AB-CD
print(solution('ABC/-AK/L-*'))  # *-A/BC-/AKL
