from .. chapter_5_orgraphs import Graph, infinity


class Graph(Graph):
    def __init__(self, number_of_vertices, start):
        self.number_of_vertices = number_of_vertices
        self.graph = [[] for _ in range(self.number_of_vertices)]
        self.vertex_in_degree = [0] * self.number_of_vertices
        self.weight = {}
        self.shortest = [infinity] * (self.number_of_vertices + 1)
        self.pred = [None] * (self.number_of_vertices + 1)
        self.start = start
