class Solution:
    def toGoatLatin(self, S: str) -> str:
        ans = []
        arr = S.split(' ')
        for i, s in enumerate(arr):
            if s[0].lower() in 'aeiou':
                x = s + 'ma'
            else:
                x = s[1:] + s[0] + 'ma'
            x += 'a' * (i + 1)
            ans.append(x)
        return ' '.join(ans)
