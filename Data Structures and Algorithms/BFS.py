from collections import deque

class Graph:

    def __init__(self, directed=False):
        self._directed = directed
        self._e = 0 # number of edges in graph
        self._adj = dict()

    # Add an edge to self between vertex v and vertex w.
    def addEdge(self, v, w):
        if not self.hasVertex(v): self._adj[v] = set()
        if not self.hasVertex(w): self._adj[w] = set()
        if not self.hasEdge(v, w):
            self._e += 1
            self._adj[v].add(w)
            if not self._directed:
                self._e += 1
                self._adj[w].add(v)

    # Return an iterable collection containing all neighbors of
    # vertex v in self.
    def adjacentTo(self, v):
        return iter(self._adj[v])

    # Return an iterable collection of all vertices in self.
    def vertices(self):
        return iter(self._adj)

    # Return True if vertex v is in self, and False otherwise.
    def hasVertex(self, v):
        return v in self._adj

    # Return True if v-w is an edge in self, and False otherwise.
    def hasEdge(self, v, w):
        return w in self._adj[v]

    # Return a string representation of self.
    def __str__(self):
        s = ''
        for v in self.vertices():
            s += v + ' -> '
            for w in self.adjacentTo(v):
                s += w + ' '
            s += '\n'
        return s

def BFS(g, s):
    # set to keep track of visited nodes
    visited = set()
    # add start node to visited
    visited.add(s)
    # queue to keep track of unvisited nodes
    queue = deque([s])
    # pred from s to d
    pred = {v: "_" for v in g.vertices()}
    while queue:
        # pop left 1st element from queue
        vertex = queue.popleft()
        # print(str(vertex) + " ", end="")

        # explore neighbours of each vertex
        for n in g.adjacentTo(vertex):
            if n not in visited:
                # if not visited then add in visited
                visited.add(n)
                # enqueue it
                queue.append(n)
                # keep track of previous vertex
                pred[n] = vertex

    return pred, visited, 

# creating graph
g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'E')
g.addEdge('B', 'D')
g.addEdge('C', 'E')
g.addEdge('C', 'F')
g.addEdge('F', 'G')
g.addEdge('F', 'H')
g.addEdge('F', 'I')

g.addEdge('J', 'K')
g.addEdge('J', 'L')
g.addEdge('K', 'L')

g.addEdge('M', 'N')

g.addEdge('O', 'P')
g.addEdge('O', 'Q')
g.addEdge('O', 'R')
g.addEdge('P', 'R')
g.addEdge('Q', 'R')


# print(g)
BFS(g, 'B')