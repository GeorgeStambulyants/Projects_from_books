infinity = float('inf')


class Graph:
    def __init__(self, number_of_vertices, start):
        self.number_of_vertices = number_of_vertices
        self.graph = [[] for _ in range(self.number_of_vertices)]
        self.vertex_in_degree = [0] * self.number_of_vertices
        self.weight = {}
        self.shortest = [infinity] * self.number_of_vertices
        self.pred = [None] * self.number_of_vertices
        self.start = start
        self.shortest[start] = 0

    def add_edge(self, from_, to, weight):
        self.graph[from_].append(to)
        self.vertex_in_degree[to] += 1
        self.weight[(from_, to)] = weight

    def get_weight(self, u, v):
        return self.weight.get((u, v))

    def relax(self, u, v):
        if self.shortest[u] + self.get_weight(u, v) < self.shortest[v]:
            self.shortest[v] = self.shortest[u] + self.get_weight(u, v)
            self.pred[v] = u

    def dijkstras_algorithm(self):
        unknown_vertices = [vert for vert in range(self.number_of_vertices)]

        while unknown_vertices:
            min_vert = unknown_vertices[0]
            for vert in unknown_vertices:
                if self.shortest[min_vert] > self.shortest[vert]:
                    min_vert = vert
            unknown_vertices.remove(min_vert)

            for v in self.graph[min_vert]:
                self.relax(min_vert, v)

    def __len__(self):
        return self.number_of_vertices


if __name__ == '__main__':
    print('TEST:')
    graph = Graph(5, 0)
    graph.add_edge(0, 1, 6)
    graph.add_edge(0, 3, 4)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 4, 4)
    graph.add_edge(3, 1, 1)
    graph.add_edge(3, 2, 9)
    graph.add_edge(3, 4, 3)
    graph.add_edge(4, 2, 5)
    graph.add_edge(4, 0, 7)
    shortest = [0, 5, 8, 4, 7]
    pred = [None, 3, 1, 0, 3]

    graph.dijkstras_algorithm()
    if graph.shortest == shortest and graph.pred == pred:
        print('OK')
    else:
         raise AssertionError(
            f'self.shortest = {graph.shortest}, shortest = {shortest}; '
            f'self.pred = {graph.pred}, pred = {pred}'
        )
