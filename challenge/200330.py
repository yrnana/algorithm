def solution(n, results):
    conn = [[False] * n for i in range(n)]

    # 자기자신과는 연결되어있음
    for i in range(n):
        conn[i][i] = True

    # 경기 결과 연결
    for a, b in results:
        conn[a - 1][b - 1] = True

    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            if conn[i][k]:
                for j in range(n):
                    if conn[k][j]:
                        # i-k가 연결되어 있고 k-j가 연결되어 있으면
                        # i-j가 연결되어 있다
                        conn[i][j] = True

    # for row in conn:
    #     print([1 if c else 0 for c in row])

    non_conn = 0
    for i in range(n):
        for j in range(n):
            if not conn[i][j] and not conn[j][i]:
                non_conn += 1
                break

    return n - non_conn


# [A, B] : A가 B를 이김
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))  # 2
print(solution(7, [[3, 7], [4, 6], [2, 3], [6, 2], [7, 1], [1, 5]]))  # 7
