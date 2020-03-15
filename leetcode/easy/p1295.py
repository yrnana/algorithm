from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                answer += 1
        return answer


solution = Solution()
print(solution.findNumbers([12, 345, 2, 6, 7896]))  # 2
print(solution.findNumbers([555, 901, 482, 1771]))  # 1
