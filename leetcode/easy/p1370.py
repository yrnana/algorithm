class Solution:
    def sortString(self, s: str) -> str:
        answer = ''
        from collections import Counter
        c = Counter(s)
        reverse = False
        while c.keys():
            answer += ''.join(sorted(c.keys(), reverse=reverse))
            delete = []
            for key in c.keys():
                c[key] -= 1
                if c[key] == 0:
                    delete.append(key)
            for key in delete:
                del c[key]
            reverse = not reverse
        return answer
