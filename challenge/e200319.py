def solution(brown, red):
    # w * h = brown + red (w >= h >= 3)
    # (w - 2) * (h - 2) = red
    answer = []
    tot = brown + red
    for h in range(3, tot):
        if tot % h == 0:
            w = tot // h
            if (w - 2) * (h - 2) == red:
                return [w, h]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
