import heapq

queue = []
graph_data = [[2, 'A'], [5, 'B'], [3, 'C']]

for edge in graph_data:
    heapq.heappush(queue, edge)
    
for index in range(len(queue)):
    print (heapq.heappop(queue))

print (queue)


from collections import defaultdict

list_dict = defaultdict(list)
print(list_dict['key1'])

list_dict2 = dict()
print(list_dict2['key1'])