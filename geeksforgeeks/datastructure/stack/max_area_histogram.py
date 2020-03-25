def solution(histogram):
    stack = []
    max_area = 0
    i = 0
    while i < len(histogram):
        print(i, stack)
        if not stack or histogram[stack[-1]] <= histogram[i]:
            stack.append(i)
            i += 1
        else:
            # h * w
            area = histogram[stack.pop()] * ((i - stack[-1] - 1) if stack else i)
            max_area = max(max_area, area)
    while stack:
        area = histogram[stack.pop()] * ((i - stack[-1] - 1) if stack else i)
        max_area = max(max_area, area)
    return max_area


print(solution([6, 2, 5, 4, 5, 1, 6]))
