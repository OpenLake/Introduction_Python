# python3 implementation of breadth first search algo for a 
# given adj matrix of a connected graph      

#Function to return the list of a BFS         
def bfs(graph, i):

    #Store the nodes in order of BFS
    #and mark them visited
    visited = []

    #Queue for BFS
    #Enqueue the source node
    queue = [i]


    while queue:
        
        #Dequeue a node from the queue
        node = queue.pop(0)

        if node not in visited:
            
            #If the graph is not visited append
            #it in the visited and start checking
            #its neighbours
            visited.append(node)
            neighbours = graph[node]
 
            #Enqueue all the neighbours which have 
            #not been visited
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)

    return visited

#driver code
if __name__ == '__main__':

    #creating graph in form of adj. matrix
    graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E', 'C'],
         'C': ['A', 'F', 'B', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']} 

print(bfs(graph,'A'))
