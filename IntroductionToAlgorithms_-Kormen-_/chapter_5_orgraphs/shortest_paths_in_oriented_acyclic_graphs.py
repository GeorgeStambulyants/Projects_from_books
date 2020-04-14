from .topological_sort import Graph


infinity = float('inf')


class Graph(Graph):
    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.graph = [[] for _ in range(self.number_of_vertices)]
        self.vertex_in_degree = [0] * self.number_of_vertices
        self.weight = {}

    def add_edge(self, from_, to, weight):
        self.graph[from_].append(to)
        self.vertex_in_degree[to] += 1
        self.weight[(from_, to)] = weight

    def get_weight(self, u, v):
        return self.weight.get(u, v)
