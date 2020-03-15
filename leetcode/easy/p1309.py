class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = ''
        i = 0
        while i < len(s):
            if (s[i] == '1' or s[i] == '2') and (i + 2 < len(s) and s[i + 2] == '#'):
                answer += chr(int(s[i:i + 2]) + 96)
                i += 3
            else:
                answer += chr(int(s[i]) + 96)
                i += 1
        return answer
