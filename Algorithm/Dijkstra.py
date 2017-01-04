#!/usr/bin/python
#
#Dijsktra's algorith
#find the shortest paths from a designated vertex to any other vertices
#
#Separate the vertices into 2 groups, spGroup includes all the vertices with shortest path calculated from starting vertext
#outGroup includes the rest of them
#
#put the starting vertex in spGroup
#store edge weight in matrix[n][n], n is the number of vertices
#set distances from starting vertex to the rest to infinite, distance is a list to store that
#FOR each edge(u,v) that only has one vertex in spGroup
#    distance[v] = min(distance[u]+matrix[u][v], distance[v])
#   

from __future__ import print_function

#N means the number of vertices
N = 9
#MAX is used as the infinite distance
MAX = 1000

class Dijkstra:
    def __init__(self):
        #matrix is initialized as a list of N empty lists [[],[],[],...[]]
        self.matrix = []
        for i in range(N):
            self.matrix.append([MAX] * N)
        for i in range(N):
            self.matrix[i][i] = 0
        #self.matrix = []
        self.distance = []
        self.edges = []
    
    def addEdges(self, u, v, weight):
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight
        self.edges.append((u,v))
        self.edges.append((v,u))
    '''
    def addEdges(self, matrix):
        self.matrix = matrix
        for i in range(N):
            for j in range(i+1, N):
                if self.matrix[i][j] != MAX:
                    self.matrix[j][i] = self.matrix[i][j]
                    self.edge.append((i, j))
                    self.edge.append((j, i))
    '''     
    def shortestPathDijkstra(self, u):
        '''
        u: the starting vertex
        '''
        for i in range(N):
            self.distance.append(MAX)
        
        spGroup = []
        spGroup.append(u)
        print(u)
        self.distance[u] = 0
        
        while len(spGroup) != N:
            min_distance = MAX
            selected_vertex = u
            for v in spGroup:
                for i in range(N):
                    if (v, i) in self.edges and i not in spGroup:
                        if self.distance[v]+self.matrix[v][i] < min_distance:
                            min_distance = self.distance[v]+self.matrix[v][i]
                            selected_vertex = i
            spGroup.append(selected_vertex)
            print(selected_vertex)
            self.distance[selected_vertex] = min_distance
            min_distance = MAX


    def printMatrix(self, u):
        print("print the matrix:")
        for i in range(N):
            for j in range(N):
                if self.matrix[i][j] == MAX:
                    print("MAX", end = '\t')
                else:
                    print("%s" % self.matrix[i][j], end = '\t')
            print("")
        print("shortest distance from %s: %s" % (u, self.distance))
            
graph = Dijkstra()
graph.addEdges(0,1,4)
graph.addEdges(0,7,8)
graph.addEdges(1,2,8)
graph.addEdges(1,7,11)
graph.addEdges(2,3,7)
graph.addEdges(2,5,4)
graph.addEdges(2,8,6)
graph.addEdges(3,4,9)
graph.addEdges(3,5,14)
graph.addEdges(4,5,10)
graph.addEdges(5,6,2)
graph.addEdges(6,7,1)
graph.addEdges(6,8,6)
graph.addEdges(7,8,7)

graph.shortestPathDijkstra(0)
graph.printMatrix(0)
