#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graph import MyGraph
from collections import deque


def BFS(graph, s):
    for v, a in graph.attributes.items():
        a['color'] = 'white'
        a['d'] = float('inf')
        a['pi'] = None
#    print(graph.adj)
    q = deque()
    graph.attributes[s]['d'] = 0
    graph.attributes[s]['pi'] = None
    graph.attributes[s]['color'] = 'gray'   #f added first vertice
    q.append(s)
    step = 0
    while len(q) > 0:
        step += 1
#        print(step, [graph.attributes[v]['name'] for v in q])
#        print(step, [graph.attributes[v]['d'] for v in q])
#        print(graph.adj[v])
#        print(q)
        x = q.popleft()
#        print(x)                                                                # take first in vertice
        for m in graph.adj[x]:                                                  # for every vertice connected with x
            if graph.attributes[m]['color'] == 'white':                         # if it newer been taken
                q.append(m)                                                     # add it to deque
                graph.attributes[m]['d'] = graph.attributes[x]['d'] + 1         # pathlenght counter
                graph.attributes[m]['pi'] = x                                   # ancestor vertice
                graph.attributes[m]['color'] = 'gray'                           # were added in deque
#            else:
#                print('eggs!')
#        print(graph.attributes)                                                  # if it was processed print stupid word
#        graph.attributes[x]['d']
        graph.attributes[x]['color'] = 'black'                                  # mark that x were processed
#        print(q)
    print(graph.attributes)
#        graph.draw('{}'.format(step))
#        raise NotImplementedError('Реализуйте алгоритм здесь')
def bfssearch(graph, s, f):
    BFS(graph, s)
    d = graph.attributes[f]['d']
    path = list()
    i = 0
    j = f
    path.append(j)
    while i < d:
        pi = graph.attributes[j]['pi']
        path.append(pi)
        j = pi
        i += 1
    print(d)
    path.reverse()
    print(path)
        

def main():
    g = MyGraph()
    g.add_vertices(8)
    for i, c in enumerate(['r', 's', 't', 'u', 'v', 'w', 'x', 'y']):
        g.attributes[i]['name'] = c

    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(2, 3)
    g.add_edge(3, 6)
    g.add_edge(3, 7)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    bfssearch(g, 1, 7)

if __name__ == "__main__":
    main()
