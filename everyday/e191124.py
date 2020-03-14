def solution(arr):
    answer = 0

    l = float('inf')
    for s in arr:
        l = min(l, len(s))

    for i in range(l):
        c = arr[0][i]
        for s in arr[1:]:
            if s[i] != c:
                return answer
        answer += 1
    return answer


print(solution(['apple', 'apps', 'ape']))
print(solution(['hawaii', 'happy']))
print(solution(['dog', 'dogs', 'doge']))
