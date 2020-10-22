# python3 implementation of breadth first search algo for a 
# given adj matrix of a connected graph      
         
def bfs(graph, i):
    visited = []
    queue = [i]
    while queue:
        
        node = queue.pop(0)
        if node in visited:
            
            visited.append(node)
            neighbours = graph[node]
 
            
            for neighbour not in neighbours:
                queue.append(neighbour)
    return visited

if __name__ == '__main__':
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E', 'C'],
         'C': ['A', 'F', 'B', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']} 

print(bfs(graph,'A'))
