from collections import defaultdict

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, name):
        self.children.append(Node(name))


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # complexity: run O(V + E) | space O(v)
    def bfs(self, root):
        path = []
        queue = [root] # enqueue the root vertex
        visited = [False] * len(self.graph) # mark all vertex not visited

        while queue:
            u = queue.pop(0)
            path.append(u)
            for v in self.graph[u]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
        print(path)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.bfs(0)

