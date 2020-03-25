def solution(name):
    answer = 0
    n = len(name)
    xmove = n - 1
    for i in range(n):
        if name[i] != 'A':
            ymove = ord(name[i]) - ord('A')
            if ymove > 13:
                ymove = 25 - ymove + 1
            answer += ymove
        next = i + 1  # 다음 문자 인덱스
        while next < n and name[next] == 'A':
            next += 1  # A가 아닐 때까지 오른쪽으로 이동
        t = n - next  # 오른쪽에서 A가 아닐때까지 이동한 총 거리
        # print({'i': i, 't': t, 'next': next, 'n': n, 'calc': i + t + min(i, t)})
        xmove = min(xmove, i + t + min(i, t))
    return answer + xmove


print("JEROEN", solution("JEROEN"))  # 56
print("JAN", solution("JAN"))  # 23
print('BBAAAAABB', solution('BBAAAAABB'))
