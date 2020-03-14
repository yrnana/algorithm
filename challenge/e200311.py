from functools import cmp_to_key


def sort_cmp(a, b):
    if a == b:
        return 1
    x, y = a + b, b + a
    if x == y or x < y:
        return 1
    else:
        return -1


def contains_only_zero(s):
    for c in s:
        if c != '0':
            return False
    return True


def solution(numbers):
    numbers = list(map(str, numbers))
    if contains_only_zero(numbers):
        return '0'
    numbers.sort(key=cmp_to_key(sort_cmp))
    return ''.join(numbers)


print(solution([6, 10, 2]))  # 6210
print(solution([3, 30, 34, 5, 9]))  # 9534330
