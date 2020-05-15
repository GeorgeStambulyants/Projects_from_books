from bellman_ford_algorithm import Graph
from collections import deque

def find_negative_weight_cycle(graph):
    '''
        bellman-ford's algorithm have been already executed
        on graph

        return list (strictly deque) that contains verteces,
        of which the cycle consists
    '''
    edges = graph.get_all_edges()
    found_edge = None
    for edge in edges:
        if graph.shortest[edge[0]] + graph.get_weight(*edge) < graph.shortest[edge[1]]:
            found_edge = edge
            break

    if not found_edge:
        return []

    visited = [False for _ in range(len(graph))]
    x = found_edge[1]
    while not visited[x]:
        visited[x] = True
        x = graph.pred[x]

    v = graph.pred[x]
    cycle = deque([x])
    while v != x:
        cycle.appendleft(v)
        v = graph.pred[v]

    return cycle


if __name__ == '__main__':
    print('TEST:')
    graph = Graph(5, 0)
    graph.add_edge(0, 1, 6)
    graph.add_edge(0, 3, 7)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, -4)
    graph.add_edge(2, 1, -2)
    graph.add_edge(3, 2, -3)
    graph.add_edge(3, 4, 9)
    graph.add_edge(4, 2, -7)
    graph.add_edge(2, 0, 2)

    graph.bellman_ford()
    neg_cycle = [4, 2, 1]
    cycle = list(find_negative_weight_cycle(graph))
    if neg_cycle == cycle:
        print('OK')
    else:
        raise AssertionError(f'{neg_cycle} != {cycle}')
