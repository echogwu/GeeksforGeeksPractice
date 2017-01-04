#!/usr/bin/python
#
#Given a graph, traverse it from a designated vertex using depth first search
#
#strategy
#
#push starting vertex into stack
#
#IF it has not been visited:
#    set it as visited
#    print it
#ENDIF
#
#IF it has outbound vertices that have not been visited:
#    pick one of the unvisited
#    recurse the process with the picked unvisited vertex
#ELSE:
#    pop the stack
#    if stack is not empty:
#        v<-stack.pop
#        recurse the process with v
#ENDIF
# 

from collections import defaultdict

class DepthFirstSearch:
    def __init__(self):
        #self.graph will be in this format: [('u',['v','x','s']),('v',['s','d'])]
        self.graph = defaultdict(list)
        self.stack = []
        self.visited = {}
        
    def addEdge(self, u, v):
        #add an edge going from u to v
        self.graph[u].append(v)
        
    def DFS(self, u):
        '''
        u: the starting vertex
        '''
        self.stack.append(u)

        if u not in self.visited:
            print(u)
            self.visited[u] = True

        count = 0
        for i in self.graph[u]:
            if i not in self.visited:
                self.DFS(i)
                break
            else:
                count += 1
        if count == len(self.graph[u]):
            self.stack.pop()
            if len(self.stack) != 0:
                self.DFS(self.stack.pop())
            
       
graph = DepthFirstSearch()
graph.addEdge(1,2)
graph.addEdge(2,4)
graph.addEdge(2,5)
graph.addEdge(4,6)
graph.addEdge(4,7)
graph.addEdge(6,8)
graph.addEdge(6,9)

graph.DFS(1)

            