class Solution:
    def binaryGap(self, N: int) -> int:
        answer = 0
        prev = -1
        i = 0
        while N > 0:
            if N % 2 == 1:
                if prev != -1:
                    answer = max(answer, i - prev)
                prev = i
            N //= 2
            i += 1
        return answer
