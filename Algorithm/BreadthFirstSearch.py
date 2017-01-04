#!/usr/bin/python
#
#Given a directed graph, traverse each vertex from a designated one
#

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        '''
        u, v: the starting and ending vertex of the directed edge
        '''
        # the data structure will be like [(1, [2, 3]), (2, [4, 5])], which stands for edeges of (1,2), (1,3), (2,4), (2,5)
        self.graph[u].append(v)

    def BFS(self, u):
        '''
        u: the designated vertex to traverse the graph from
        '''
        # use a queue to store vertices waiting to be visited
        queue = []

        # to avoid infinite loop, use a list to mark each vertex as visited or not, if the vertex is of type int, we can use a list instead of a dictionary
        visited = {}

        queue.append(u)
        visited[u] = True

        while len(queue):
            vertex = queue.pop(0)
            print(vertex)

            for i in self.graph[vertex]:
                # must not forget to check if i is in the visited
                if i not in visited:
                    queue.append(i)
                    visited[i] = True

# test if the class works
graph = Graph()

'''
graph.addEdge('p','s')
graph.addEdge('p','u')
graph.addEdge('s','p')
graph.addEdge('s','f')
graph.addEdge('u','f')
graph.addEdge('d','s')
graph.addEdge('f','d')
graph.addEdge('u','g')
graph.addEdge('g','d')
graph.addEdge('d','h')

graph.BFS('d')
'''
graph.addEdge(1,2)
graph.addEdge(1,7)
graph.addEdge(6,1)
graph.addEdge(4,1)
graph.addEdge(1,7)
graph.addEdge(2,3)
graph.addEdge(2,4)
graph.addEdge(3,2)
graph.addEdge(5,4)
graph.addEdge(3,5)
graph.addEdge(5,6)

graph.BFS(1)




