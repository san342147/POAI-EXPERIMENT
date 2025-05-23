class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        if v in self.graph:
            for neighbour in self.graph[v]:
                if not visited[neighbour]:
                    self.dfs_util(neighbour, visited)

    def dfs(self, v):
        visited = [False] * 6
        print("Depth First Search starting from vertex", v, end=':\n')
        self.dfs_util(v, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

g.dfs(0)
