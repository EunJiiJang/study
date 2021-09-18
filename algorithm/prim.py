from collections import defaultdict
from heapq import*

myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

def prim(start_node,edges):
    mst = list()
    adj_edges = defaultdict(list)
    for weight,n1,n2 in edges:
        adj_edges[n1].append((weight,n1,n2))
        adj_edges[n2].append((weight,n2,n1))
    
    connected_node = set(start_node)
    candidate_edge_list = adj_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight,n1,n2 = heappop(candidate_edge_list)
        if n2 not in connected_node:
            connected_node.add(n2)
            mst.append((weight,n1,n2))

            for edge in adj_edges[n2]:
                if edge[2] not in connected_node:
                    heappush(candidate_edge_list,edge)
    return mst

print(prim('A',myedges))

