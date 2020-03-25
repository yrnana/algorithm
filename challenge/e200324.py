def solution(baseball):
    from itertools import permutations

    def check(number, question, strike, ball):
        question, s, b = str(question), 0, 0
        for i in range(3):
            if number[i] == question[i]:
                s += 1
            elif question[i] in number:
                b += 1
        return s == strike and b == ball

    baseball.sort(key=lambda x: x[1])  # s 우선 정렬
    p = permutations(range(1, 10), 3)
    arr = [''.join(list(map(str, t))) for t in p]
    for num, s, b in baseball:
        tmp = []
        while arr:
            n = arr.pop()
            if check(n, num, s, b):
                tmp.append(n)
        arr = tmp
    return len(arr)


print(solution([[123, 1, 1], [356, 1, 0], [489, 0, 1], [489, 0, 1]]))  # 2
