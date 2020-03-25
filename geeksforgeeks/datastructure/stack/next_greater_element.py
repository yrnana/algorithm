# 오른쪽에서 자기자신보다 큰수로 첫번째로 나타나는 수 (next greater element)
# 왼쪽 수들을 스택에 저장해두고 nge를 찾으면 뺀다


def solution(arr):
    ans = []
    stack = [arr[0]]
    for i in range(1, len(arr)):
        j = arr[i]
        if stack:
            x = stack.pop()
            while x < j:
                ans.append((x, j))
                if not stack:
                    break
                x = stack.pop()
            if x > j:
                stack.append(x)
        stack.append(j)
    while stack:
        ans.append((stack.pop(), -1))
    return ans


print(solution([11, 13, 21, 3]))
print(solution([4, 5, 2, 25]))
