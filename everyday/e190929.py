def solution(arr):
    answer = [arr[0]]
    for a in arr[1:]:
        tmp_answer = []
        while any(answer):
            b = answer.pop(0)
            if a[1] < b[1]:
                x0, y0 = a
                x1, y1 = b
            else:
                x0, y0 = b
                x1, y1 = a
            if y0 < x1:
                tmp_answer.append(a)
                tmp_answer.append(b)
            else:
                tmp_answer.append([min(x0, x1), max(y0, y1)])
        answer = tmp_answer
    return answer


print(solution([[2, 4], [1, 5], [7, 9]]))
print(solution([[3, 6], [1, 3], [2, 4]]))
