class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1. level 'l'의 노드 수는 최대 2^(l-1)
# 2. height 'h'의 노드 수는 최대 2^h-1
# 3. N 노드를 가지는 트리에서 최소 l or h = log_2(N+1)
# 4. l leaves를 가지는 트리는 최소 log_2(L) levels
# 5. Full Binary tree는 leaves = internal + 1
