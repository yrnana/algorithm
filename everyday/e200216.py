# gcd : 유클리드 호제법
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solution(arr):
    ans = gcd(arr[0], arr[1])
    for x in arr[2:]:
        ans = gcd(ans, x)
        if ans == 1:
            return 1
    return ans


print(solution([3, 2, 1]))
print(solution([2, 4, 6, 8]))
