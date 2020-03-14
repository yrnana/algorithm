dmap = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F',
}


def number2base(n, b):
    if n == 0:
        return '0'
    digits = ''
    while n:
        digits = dmap[str(n % b)] + digits
        n //= b
    return digits


def solution(n, t, m, p):
    answer = ''
    tmp = ''
    i = 0
    while len(tmp) < t * m:
        s = number2base(i, n)
        tmp += s
        i += 1
    for j in range(len(tmp)):
        if j % m == p - 1:
            answer += tmp[j]
            if len(answer) == t:
                break
    return answer


print(solution(2, 4, 2, 1))  # 0111
print(solution(16, 16, 2, 1))  # 02468ACE11111111
print(solution(16, 16, 2, 2))  # 13579BDF01234567
