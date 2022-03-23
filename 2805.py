from sys import stdin
input = stdin.readline

def slice_max(list, need, start, end):
    global max_tree
    if start > end:
        print(max_tree)
        return
        
    mid = (start + end) // 2
    current = 0

    for tree in list:
        if tree >= mid:
            current += tree - mid
    
    if current >= need:
        max_tree = max(max_tree, mid)
        slice_max(list, M, mid+1, end)
    else:
        slice_max(list, M, start, mid-1)


N, M = map(int, input().split())
tree_height = list(map(int, input().split()))

max_tree = 0
max_height = max(tree_height)

slice_max(tree_height, M, 0, max_height)