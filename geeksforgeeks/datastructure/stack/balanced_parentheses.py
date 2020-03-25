def solution(exp):
    s = []
    for c in exp:
        if c == '(' or c == '[' or c == '{':
            s.append(c)
            continue
        if not s:
            return False
        if c == ')':
            if s.pop() != '(':
                return False
        elif c == '}':
            if s.pop() != '{':
                return False
        elif c == ']':
            if s.pop() != '[':
                return False
    return not s


print(solution('[()]{}{[()()]()}'))
print(solution('[(])'))
print(solution('[()]]'))
