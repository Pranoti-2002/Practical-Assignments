from collections import deque
def shortest_path_bfs(graph , source):
    num_vertices=len(graph) 

    distances=[-1]*num_vertices
    visited=[False]*num_vertices 

    distances[source]=0 
    queue=deque() 
    queue.append(source) 
    while queue:
        vertex=queue.popleft()
        visited[vertex]=True 
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                if distances[neighbor]==-1:
                    distances[neighbor]=distances[vertex]+1 
                    queue.append(neighbor) 
    return distances 

graph={ 
    0:[1 , 2] ,
    1:[2 , 3] ,
    2:[3 , 4] ,
    3:[4] , 
    4:[] 
} 

source_vertex=0 
distances=shortest_path_bfs(graph, source_vertex) 

for vertex , distance in enumerate(distances):
    print(f"shortest distance from {source_vertex} to {vertex}: {distance}") 