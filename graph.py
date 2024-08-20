class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.add(vertex)
            self.adjacency_list[vertex] = set()

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            self.vertices.remove(vertex)
            del self.adjacency_list[vertex]
            self.edges = {(u, v) for u, v in self.edges if u != vertex and v != vertex}
            for adj in self.adjacency_list.values():
                adj.discard(vertex)

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.edges.add((u, v))
            self.adjacency_list[u].add(v)
            self.adjacency_list[v].add(u)

    def remove_edge(self, u, v):
        if (u, v) in self.edges:
            self.edges.remove((u, v))
            self.adjacency_list[u].discard(v)
            self.adjacency_list[v].discard(u)

    def is_adjacent(self, u, v):
        return v in self.adjacency_list.get(u, set())

    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, set())

    def __repr__(self):
        return f"Graph(vertices={self.vertices}, edges={self.edges})"
