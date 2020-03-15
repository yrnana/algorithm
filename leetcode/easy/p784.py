from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        answer = []
        self.recur(answer, '', 0, S)
        return answer

    def recur(self, ans, curr, i, S):
        if i == len(S):
            ans.append(curr)
            return
        if S[i].isalpha():
            self.recur(ans, curr + S[i].lower(), i + 1, S)
            self.recur(ans, curr + S[i].upper(), i + 1, S)
        else:
            self.recur(ans, curr + S[i], i + 1, S)
