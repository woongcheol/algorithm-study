class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
def pre_ord(node):
    print(node.value, end = '')
    if node.left != '.':
        pre_ord(tree[node.left])
    if node.right != '.':
        pre_ord(tree[node.right])

def in_ord(node):
    if node.left != '.':
        in_ord(tree[node.left])
    print(node.value, end = '')
    if node.right != '.':
        in_ord(tree[node.right])

def post_ord(node):
    if node.left != '.':
        post_ord(tree[node.left])
    if node.right != '.':
        post_ord(tree[node.right])
    print(node.value, end = '')

N = int(input())
tree = dict()
for _ in range(N):
    value, left, right = input().split()
    tree[value] = Node(value, left, right)

pre_ord(tree['A'])
print()
in_ord(tree['A'])
print()
post_ord(tree['A'])