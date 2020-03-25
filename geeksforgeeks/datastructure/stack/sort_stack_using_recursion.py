def sorted_insert(s, element):
    if not s or element > s[-1]:
        s.append(element)
        return
    tmp = s.pop()
    sorted_insert(s, element)
    s.append(tmp)


def sort_stack(s):
    if s:
        tmp = s.pop()
        sort_stack(s)
        sorted_insert(s, tmp)  # sorted 된 스택에 tmp를 넣는다


stack = [-3, 14, 18, -5, 30]
print(stack)
sort_stack(stack)
print(stack)
