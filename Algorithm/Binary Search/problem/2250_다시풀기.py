# 노드 클래스
class Node():
    def __init__(self, number, left_node, right_node):
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node

# 중위 순회 함수
def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(tree[node.left_node], level + 1)
    level_min[level] = min(level_min[tree], x)
    level_max[level] = max(level_max[tree], x)
    x += 1
    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)

# 변수 선언 및 할당
tree = {}
N = int(input())
level_min = [N]
level_max = [0]
root = -1
x = 1
level_depth = 1

# 노드 수 만큼 노드, 레벨 최솟값, 최대값 생성
for idx in range(1, N+1):
    tree[idx] = Node(idx, -1, -1)
    level_min.append(N)
    level_max.append(0)

# 노드 생성
for _ in range(N):
    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node

    # 부모 노드 지정
    if left_node != -1:
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number

# 노드 탐색 및 루트 노드 지정
for i in range(1, N+1):
    if tree[i].parrent == -1:
        root = i

# 중위 순회
in_order(tree[root], 1)