def solution(heights):
    answer = [0]
    stack = [(1, heights[0])]
    for i in range(1, len(heights)):
        while stack and stack[-1][1] <= heights[i]:
            stack.pop()
        answer.append(stack[-1][0] if stack else 0)
        stack.append((i + 1, heights[i]))
    return answer


print(solution([6, 9, 5, 7, 4]))  # [0, 0, 2, 2, 4]
print(solution([3, 9, 9, 3, 5, 7, 2]))  # [0, 0, 0, 3, 3, 3, 6]
print(solution([1, 5, 3, 6, 7, 6, 5]))  # [0, 0, 2, 0, 0, 5, 6]
