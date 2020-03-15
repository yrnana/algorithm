class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a, b = 1, 0
        while n > 0:
            r = n % 10
            a *= r
            b += r
            n //= 10
        return a - b
