import heapq 

def prim(graph):
    mst=[] 
    visited=set() 

    start_vertex=list(graph.keys())[0] 
    visited.add(start_vertex) 

    pq=[] 
    for neighbor , weight in graph[start_vertex]:
        heapq.heappush(pq, (weight , start_vertex , neighbor)) 
    while pq:
        weight , u , v=heapq.heappop(pq) 
        if v not in visited:
            visited.add(v) 
            mst.append((u , v , weight)) 
            for neighbor , weight in graph[v]:
                heapq.heappush(pq, (weight , v , neighbor))  
    return mst 
graph={ 
    'A':[('B' , 2) , ('C' , 4)] ,
    'B':[('A' , 2) , ('D' , 9) , ('E' , 1)],
    'C':[('A' , 4) , ('D' , 6)] , 
    'D':[('B' , 9) , ('C' , 6)] , 
    'E':[('B' , 1) , ('D' , 3)] 
} 

minimum_spanning_tree=prim(graph) 
for edge in minimum_spanning_tree:
    u , v , weight=edge 
    print(f'{u} -- {v} : {weight}') 