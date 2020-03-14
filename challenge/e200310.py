# 유클리드 호제법 : 두 수의 최대공약수
# 두 수 a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면 (단, a > b),
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


# 두 수의 최소공배수
def lcm(x, y):
    return x * y // gcd(x, y)


def solution(arr):
    # arr 원소가 하나라면 최대공배수는 자기 자신
    if len(arr) == 1:
        return arr[0]

    # 여러수의 최소공배수
    # a, b의 최소공배수 l -> l, c의 최소공배수 -> ...
    ans = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        ans = lcm(ans, arr[i])

    return ans


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
print(solution([5, 7, 9]))
print(solution([12, 36, 30, 24]))
