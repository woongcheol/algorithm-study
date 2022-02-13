# Kruskal's algorithm
# graph 생성
# mygraph = {
#     'vertices':['A', 'B', 'C', 'D', 'E', 'F', 'G'],
#     'edges':[
#         (7, 'A', 'B'),
#         (5, 'A', 'D'),
#         (7, 'B', 'A'),
#         (8, 'B', 'C'),
#         (9, 'B', 'D'),
#         (7, 'B', 'E'),
#         (8, 'C', 'B'),
#         (5, 'C', 'E'),
#         (5, 'D', 'A'),
#         (9, 'D', 'B'),
#         (7, 'D', 'E'),
#         (6, 'D', 'F'),
#         (7, 'E', 'B'),
#         (5, 'E', 'C'),
#         (7, 'E', 'D'),
#         (8, 'E', 'F'),
#         (9, 'E', 'G'),
#         (6, 'F', 'D'),
#         (8, 'F', 'E'),
#         (11, 'F', 'G'),
#         (9, 'G', 'E'),
#         (11, 'G', 'F')
#     ]
# }

# # 자료형 생성
# parent = dict()
# rank = dict()

# def find(node):
#     # path compression 기법
#     if parent[node] != node:
#         parent[node] = find(parent[node])
#     return parent[node]

# def union(node_v, node_u):
#     root1 = find(node_v)
#     root2 = find(node_u)

#     # union-by-rank 기법
#     if rank[root1] > rank[root2]:
#         parent[root2] = root1
#     else:
#         parent[root1] = root2
#         if rank[root1] == rank[root2]:
#             rank[root2] += 1

# def make_set(node):
#     parent[node] = node
#     rank[node] = 0

# # kruskal 함수 생성
# def kruskal(graph):
#     mst = list()

#     # 1. 초기화
#     for node in graph['vertices']:
#         make_set(node)

#     # 2. 간선 weight 기반 sorting
#     edges = graph['edges']
#     edges.sort()

#     # 3. 사이클 없는 간선만 연결
#     for edge in edges:
#         weight, node_v, node_u = edge
#         if find(node_v) != find(node_u):
#             union(node_v, node_u)
#             mst.append(edge)
        
#     return mst

# print(kruskal(mygraph))

# Prim's Algorithm

myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

from collections import defaultdict
from heapq import *

def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)
    
    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))
            
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst

print(prim ('A', myedges))