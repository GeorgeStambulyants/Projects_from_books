import dijkstras_algorithm as dij_al


class Graph(dij_al.Graph):
    def __init__(self, number_of_vertices, start):
        super().__init__(number_of_vertices, start)

    def get_all_edges(self):
        '''
            returns a list of all edges
        '''
        edges = []
        for u in range(self.number_of_vertices):
            for v in self.graph[u]:
                edges.append((u, v))
        return edges

    def bellman_ford(self):
        '''
            this algorithm works even with negative weights
        '''
        edges = self.get_all_edges()
        for i in range(1, self.number_of_vertices):
            for edge in edges:
                self.relax(*edge)
