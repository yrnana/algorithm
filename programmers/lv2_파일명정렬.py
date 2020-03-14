from functools import cmp_to_key


def sort_cmp(x0, x1):
    h0, n0, t0 = x0
    h1, n1, t1 = x1
    h0, h1 = h0.lower(), h1.lower()
    if h0 < h1:
        return -1
    elif h0 > h1:
        return 1
    n0, n1 = int(n0), int(n1)
    if n0 < n1:
        return -1
    elif n0 > n1:
        return 1
    return 1


def solution(files):
    answer = []
    for file in files:
        head = ''
        number = ''
        i = 0
        for c in file:
            if not c.isdecimal():
                if len(number) > 0:
                    break
                head += c
            else:
                number += c
            i += 1
        tail = file[i:]
        answer.append((head, number, tail))
    answer.sort(key=cmp_to_key(sort_cmp))
    return [''.join(x) for x in answer]


# print(solution(['foo9.txt', 'foo010bar020.zip', 'F-15']))
print(solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']))
print(solution(['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']))
