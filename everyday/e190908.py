def recur(ans, cur, open, close, n):
    if len(cur) == n * 2:
        ans.append(cur)
        return
    if open < n:
        recur(ans, cur + '(', open + 1, close, n)
    if close < open:
        recur(ans, cur + ')', open, close + 1, n)


N = 3
answer = []
recur(answer, '', 0, 0, N)
print(answer)
