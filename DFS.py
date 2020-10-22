# This is a Python3 program to print DFS traversal  
# for a given connected given graph 

from collections import defaultdict 

class Graph: 

	def __init__(self):  
		self.graph = defaultdict(list) 

	def addEdge(self, u, v): 
		self.graph[u].append(u) 

	def DFSUtil(self, v, visited): 
		visited[v] = True
		print(v, end = ' ') 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.DFSUtil(i, visited) 

	def DFS(self, v): 

		visited = [True] * (max(self.graph)+1) 
		self.DFSUtil(u, visited) 

# Driver code 
if __name__ == '__main__':
	g = Graph() 
	g.addEdge(0, 1) 
	g.addEdge(1, 2) 
	g.addEdge(3, 2) 
	g.addEdge(2, 0) 
	g.addEdge(0, 3) 
	g.addEdge(3, 1)
	g.addEdge(4, 2)

	print("DFS for the given graph starting from vertex 0 is :") 
	g.DFS(0) 

