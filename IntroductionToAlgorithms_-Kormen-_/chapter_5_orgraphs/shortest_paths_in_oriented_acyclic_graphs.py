# Time: O(n + m), where n -- number of vertices and m -- number of edges

from topological_sort import Graph


infinity = float('inf')


class Graph(Graph):
    def __init__(self, number_of_vertices):
        '''
            in self.shortest each index represents respective vertex
            and its value represents the shortest path to
            it from fiction_start, i.e.
            the shortest path from any other vertex
        '''
        self.number_of_vertices = number_of_vertices
        self.graph = [[] for _ in range(self.number_of_vertices)]
        self.vertex_in_degree = [0] * self.number_of_vertices
        self.weight = {}
        self.shortest = [infinity] * (self.number_of_vertices + 1)
        self.pred = [None] * (self.number_of_vertices + 1)
        self.fiction_start = number_of_vertices
        self.shortest[self.fiction_start] = 0
        self.pred[self.fiction_start] = None

    def add_edge(self, from_, to, weight):
        self.graph[from_].append(to)
        self.vertex_in_degree[to] += 1
        self.weight[(from_, to)] = weight

    def get_weight(self, u, v):
        return self.weight.get(u, v)

    def relax(self, u, v):
        if self.shortest[u] + self.get_weight(u, v) < self.shortest[v]:
            self.shortest[v] = self.shortest[u] + self.get_weight(u, v)
            self.pred[v] = u

    def dag_shortest_paths(self):
        linear_order = self.topological_sort()

        for i in range(len(self.number_of_vertices)):
            self.shortest[i] = infinity
            self.pred[i] = None
        self.shortest[self.number_of_vertices] = 0

        for u in linear_order:
            for v in self.graph[u]:
                self.relax(u, v)
