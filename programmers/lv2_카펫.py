def solution(brown, red):
    # a * b = brown + red
    # a + b = (brown + 4) / 2
    x = brown + red
    y = (brown + 4) / 2
    for i in range(3, x):
        if x % i == 0 and (i + x // i) == y:
            return [x // i, i]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
