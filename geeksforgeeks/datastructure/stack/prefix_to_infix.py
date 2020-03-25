def solution(exp):
    stack = []
    for c in exp[::-1]:
        if c.isalpha():
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append('(' + op1 + c + op2 + ')')
    return stack[-1][1:-1]


print(solution('*+AB-CD'))  # (A+B)*(C-D)
print(solution('*-A/BC-/AKL'))  # (A-(B/C))*((A/K)-L)
