class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer = 0
        r, l = 0, 0
        for c in s:
            if c == 'R':
                r += 1
            else:
                l += 1
            if r == l:
                answer += 1
                r, l = 0, 0
        return answer
