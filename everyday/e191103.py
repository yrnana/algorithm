def solution(A, B):
    ab, ba = dict(), dict()
    for i in range(len(A)):
        a, b = A[i], B[i]
        if a in ab and ab[a] != b:
            return False
        if b in ba and ba[b] != a:
            return False
        ab[a] = b
        ba[b] = a
    return True


print(solution("EGG", "FOO"))
print(solution("ABBCD", "APPLE"))
print(solution("AAB", "FOO"))
