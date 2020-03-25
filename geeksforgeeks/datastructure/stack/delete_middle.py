def delete_middle(s, n, curr):
    if not s or curr == n:
        return
    x = s.pop()
    delete_middle(s, n, curr + 1)
    if curr != n // 2:
        s.append(x)


stack = [1, 2, 3, 4, 5, 6, 7]
delete_middle(stack, len(stack), 0)
print(stack)
