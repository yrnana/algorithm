def evaluate(nums, ops):
    val2 = nums.pop()
    val1 = nums.pop()
    op = ops.pop()
    nums.append(str(eval(val1 + op + val2)))


def solution(exp):
    tokens = exp.split(' ')
    rank = {'+': 1, '-': 1, '*': 2, '/': 2}
    nums, ops = [], []
    for t in tokens:
        if t.isdecimal():
            nums.append(t)
        elif t == '(':
            ops.append(t)
        elif t == ')':
            while ops and ops[-1] != '(':
                evaluate(nums, ops)
            ops.pop()  # remove ')'
        else:
            while ops and ops[-1] in rank and rank[t] <= rank[ops[-1]]:
                evaluate(nums, ops)
            ops.append(t)
    while ops:
        evaluate(nums, ops)
    return float(nums[-1])


# print(solution("10 + 2 * 6"))
# print(solution("100 * 2 + 12"))
# print(solution("100 * ( 2 + 12 )"))
# print(solution("100 * ( 2 + 12 ) / 14"))
print(solution("10 + 100 * ( 2 + 12 ) / 14"))
