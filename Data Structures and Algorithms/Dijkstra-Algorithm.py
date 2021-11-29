# Dijkstra Algorithm - Find Shortest Path

import heapq
import itertools


class Graph:

    # Construct a new Graph object. If a filename is specified,
    # populate the Graph object by reading data from the specified
    # file with the specified delimiter.
    # For directed graphs the argument directed should get value True
    def __init__(self,  filename=None, directed=False, delimiter=None):
        self._directed = directed
        self._e = 0
        self._adj = dict()
        if filename is not None:
            f = open(filename, 'r')
            lines = f.read().split('\n')
            for line in lines:
                names = line.split(delimiter)
                for i in range(1, len(names), 2):
                    self.addEdge(names[0], names[i], float(names[i+1]))
            line = ''
            f.close()

    # Add an edge to self between vertex v and vertex w.
    def addEdge(self, v, w, weight):
        if not self.hasVertex(v): self._adj[v] = set()
        if not self.hasVertex(w): self._adj[w] = set()
        if not self.hasEdge(v, w, weight):
            self._e += 1
            self._adj[v].add((w, weight))
            if not self._directed:
                self._e += 1
                self._adj[w].add((v, weight))

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
    def hasEdge(self, v, w, weight):
        return (w, weight) in self._adj[v]

    # Return the number of vertices in self.
    def countV(self):
        return len(self._adj)

    # Return the number of edges in self.
    def countE(self):
        return self._e

    # Return the degree of vertex v of self.
    def degree(self, v):
        return len(self._adj[v])

    # Return a string representation of self.
    def __str__(self):
        s = ''
        for v in self.vertices():
            s += v + '  '
            for w in self.adjacentTo(v):
                s += w[0] + ' ' + str(w[1]) + ' '
            s += '\n'
        return s

class PriorityQ:
    def __init__(self):
        # the heap: entries will be prio, counter, object
        # the counter is generated in the class
        self._pq = []
        # a dictionary for entries that are in the heap
        self._entry_finder = {}
        self._REMOVED = '<removed-task>'      # placeholder for a removed task
        self._counter = itertools.count()     # unique sequence count

    def isEmpty(self):
        return len(self._entry_finder) == 0

    def insert(self, obj, priority):
        if obj in self._entry_finder:
            self._remove(obj)
        count = next(self._counter)
        entry = [priority, count, obj]
        # important: both entry_finder[obj] and the pq are pointing
        # to the same object.
        # When we modify it via entry_finder we also modify it in pq!
        self._entry_finder[obj] = entry
        heapq.heappush(self._pq, entry)

    def __contains__(self, obj):
        return obj in self._entry_finder

    def decrease_key(self, obj, prio):
        self.remove(obj)
        self._insert(obj, prio)

    def remove(self, obj):
        # Mark an existing task as REMOVED.
        # Raise KeyError if not found.
        entry = self._entry_finder.pop(obj)
        # mark gets registered in pq also as (prio, count, REMOVED)
        entry[-1] = self._REMOVED

    def pop(self):
    # Remove and return the lowest priority task.
    # Raise KeyError if empty.'
    # Pops all REMOVED with low priorities
        while self._pq != [] :
            priority, count, obj = heapq.heappop(self._pq)
            if obj is not self._REMOVED:
                del self._entry_finder[obj]
                return obj
        raise KeyError('pop from an empty priority queue')

    def __str__(self):
        return str(self._pq)



def d_shortest_paths(g, s, d):
    # INFINITY is something that depends on the domain that the graph
    # is supposed to model.
    # you might want /need to change it if your weights can be larger!
    INFINITY = 1000000.0
    visited = set()
    # distTo[v] = shortest path distance from s to v among visited nodes
    distTo = {v : INFINITY for v in g.vertices()}
    distTo[s] = 0

    pq = PriorityQ()
    for v in g.vertices():
        pq.insert(v, distTo[v])

    previous = {v : "_" for v in g.vertices()}

    while not pq.isEmpty():
        v = pq.pop()
        visited.add(v)
        for w, weight in g.adjacentTo(v):
            if w not in visited:
                pq.remove(w)
                if (distTo[v] + weight) < distTo[w]:
                    distTo[w] = distTo[v] + weight
                    # keep track of previous node
                    previous[w] = v
                pq.insert(w, distTo[w])


    # let's print shortest route
    path = [d]
    for n in list(previous):
        if path[-1] == s:
            break
        path.append(previous[path[-1]])
            
    path.reverse()
    print(*path, sep=' -> ')
    print("Total Distance From ", s, " to ", d, " is ", distTo[d])

    
## find shortest path
g = Graph('test.txt', False, ' ')
d_shortest_paths(g, 'PakGate', '9No')