from .topological_sort import Graph

infinity = float('inf')


class Graph(Graph):
    def __init__(self, number_of_vertices: int):
        self.start = 0
        self.number_of_vertices = number_of_vertices
        self.shortest = [0] + [infinity] * self.number_of_vertices
        self.pred = [None] * (self.number_of_vertices + 1)
        self.graph = {
            vertex: [] for vertex in range(1, self.number_of_vertices + 1)
        }
        self.weights = {}

    def add_edge(self, from_: int, to: int, weight: int):
        self.graph[from_].append(to)
        self.weights.update({
            (from_, to): weight,
        })

    def get_weight(u: int, v: int) -> int:
        return self.weights.get(u, v)

    def relax(u: int, v: int):
        '''
            u, v - two vertices
            (u, v) - edge
        '''
        if self.shortest[u] + self.get_weight(u, v) < self.shortest[v]:
            self.shortest[v] = self.shortest[u] + self.get_weight(u, v)
            self.pred[v] = u
