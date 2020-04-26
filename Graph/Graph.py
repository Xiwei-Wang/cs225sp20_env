'''
MIT License

Name cs225sp20_env Python Package
URL https://github.com/Xiwei-Wang/cs225sp20_env

Version 1.0
Creation Date 26 April 2020

Copyright(c) 2020 Instructors, TAs and Some Students of UIUC CS 225 SP20 ZJUI Course
Instructorts: Prof. Dr. Klaus-Dieter Schewe
TAs: Tingou Liang, Run Zhang, Enyi Jiang, Xiang Li
Group 1 Students: Shen Zheng, Haozhe Chen, Ruiqi Li, Xiwei Wang
Other Students: Zhongbo Zhu

Above all, due to academic integrity, students who will take UIUC CS 225 ZJUI Course
taught with Python later than Spring 2020 semester are NOT authorized with the access
to this package.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files(the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
---------
File cs225sp20_env/Graph/Graph.py
Version 1.0
'''
# %%
# for VS Code users
if __name__ != "cs225sp20_env.Graph.Graph":
    import sys
    sys.path.append(__file__[:-len("cs225sp20_env/Graph/Graph.py")])
# %%
# for PyCharm users
if __name__ != "cs225sp20_env.Graph.Graph":
    import sys
    import os
    sys.path.append(os.getcwd())
# %%
from cs225sp20_env.Graph.VertexList import VertexList
from cs225sp20_env.Graph.EdgeList import EdgeList
from cs225sp20_env.List.PyList import PyList
from cs225sp20_env.List.Fifo import Fifo
# %%
class Graph:
    def __init__(self,edges=[]):
        self.vertexList = VertexList(edges)
        for e in edges:
            self.addEdge(e)
            self.addEdge((e[1],e[0]))

    def addEdge(self,edge):
        vertex = self.vertexList.locate(edge[0])
        edgelist = vertex.edges
        if edgelist != None:
            edgelist.add(edge[1])
        else:
            edgelist = EdgeList(edge[1])
        vertex.setEdges(edgelist)

    def __iter__(self):
        vertices = self.vertexList
        for v in vertices:
            x = vertices.locate(v)
            y = x.edges
            if y != None:
                for z in y:
                    yield (v,z)

    def insertVertex(self,item):
        if not (item in self.vertexList):
            self.vertexList.append(item)

    def deleteVertex(self,item):
        return self.vertexList.remove(item)

    def insertEdge(self,edge):
        self.vertexList.addVertex(edge)
        self.addEdge(edge)
        self.addEdge((edge[1],edge[0]))

    def deleteEdge(self,edge):
        self.__deleteEdge(edge)
        self.__deleteEdge((edge[1],edge[0]))

    def __deleteEdge(self,edge):
        if not (edge[0] in self.vertexList):
            print("There is no edge", edge)
            return False
        vertexlocation = self.vertexList.locate(edge[0])
        edgelist = vertexlocation.getEdges()
        if edgelist == None:
            print("There is no edge", edge)
            return False
        res = edgelist.remove(edge[1])
        if res == False:
            print("There is no edge", edge)
        return res

    def outgoingEdges(self,item):
        vertex = self.vertexList.locate(item)
        if vertex == None:
            print("There is no vertex", item)
            return []
        edgelist = vertex.getEdges()
        if edgelist == None:
            return []
        res = []
        for v in edgelist:
            res.append((item,v))
        return res
            # yield (item,v) # If we replace the above two lines with this line, then this methods works as an iterator.
    
    def bfs_KD(self,vertex):
        if not (vertex in self.vertexList):
            print("There is no vertex", vertex)
            return None
        length = self.vertexList.getlength()
        distance = [None] * length
        parent = [None] * length
        index = self.vertexList.index(vertex)
        distance[index] = 0
        parent[index] = vertex
        currentlayer = Fifo(length)
        currentlayer.pushback(vertex)
        nextlayer = Fifo(length)
        for l in range(length):
            for u in currentlayer:
                # print(u)
                loc = self.vertexList.locate(u)
                edgelist = loc.getEdges()
                if edgelist != None:
                    for v in edgelist:
                        idx = self.vertexList.index(v)
                        if parent[idx] == None:
                            nextlayer.pushback(v)
                            distance[idx] = l + 1
                            parent[idx] = u
            currentlayer = nextlayer
            nextlayer = Fifo(length)
        return (distance,parent)

    def bfs(self,vertex,index):
        if not (vertex in self.vertexList):
            print("There is no vertex", vertex)
            return None
        length = self.vertexList.getlength()
        self.distance[index] = 0
        self.parent[index] = vertex
        queue = []
        queue.append(vertex)
        head = 0 # head index of queue
        while head < len(queue):
            u = queue[head]
            index = self.vertexList.index(u)
            cur_distance = self.distance[index]
            loc = self.vertexList.locate(u)
            edgelist = loc.getEdges()
            if edgelist != None:
                for v in edgelist:
                    idx = self.vertexList.index(v)
                    if self.parent[idx] == None:
                        queue.append(v)
                        self.distance[idx] = cur_distance + 1
                        self.parent[idx] = u
                    else:
                        # TODO leave space to handle if meet other vertex in the same subset
                        pass
            head += 1

    def allBFS(self):
        numVertices = self.vertexList.getlength()
        self.distance = [None] * numVertices
        self.parent = [None] * numVertices
        for s in self.vertexList:
            idx = self.vertexList.index(s)
            if self.distance[idx] == None:
                self.bfs(s,idx)
        return (self.distance,self.parent)

    #DFS traverse using recursion
    def allDFS(self):
        numVertices = self.vertexList.getlength()
        initlist = [None]* numVertices
        self.tree = PyList(initlist,numVertices)
        for i in range(numVertices):
            newgraph = Graph([])
            self.tree[i] = newgraph
        self.mark = [None] * numVertices
        self.dfsPos = 1
        self.dfsNum = [1] * numVertices
        self.finishingTime = 1
        self.finishTime = [1] * numVertices
        for s in self.vertexList:
            idx = self.vertexList.index(s)
            if self.mark[idx] == None:
                self.mark[idx] = s
                self.dfsNum[idx] = self.dfsPos
                self.dfsPos += 1
                self.dfs(s,idx)

    def dfs(self,vertex,index):
        for e in self.outgoingEdges(vertex):
            idx = self.vertexList.index(e[1])
            if self.mark[idx] == None:
                self.tree[index].insertEdge(e)
                self.__traverseTreeEdge(e)
                self.mark[idx] = e[1]
                self.dfs(e[1],index)
        self.backtrack(vertex)

    def __traverseTreeEdge(self,e):
        idx = self.vertexList.index(e[1])
        self.dfsNum[idx] = self.dfsPos
        self.dfsPos += 1

    def backtrack(self,vertex):
        idx = self.vertexList.index(vertex)
        self.finishTime[idx] = self.finishingTime
        self.finishingTime += 1
# %%
if __name__ == "__main__":
    edges = [(1,2),(2,4),(3,5),(2,5),(1,5),(3,4),(3,1),(6,2),(6,3)]
    g = Graph(edges)
    print(g.outgoingEdges(1))
    print([v for v in g.vertexList])
    g.insertVertex(7)
    g.insertVertex(8)
    print([v for v in g.vertexList])
    g.deleteVertex(1)
    g.deleteVertex(7)
    print([v for v in g.vertexList])
    print([e for e in g])
    g.insertEdge((1,7))
    print([e for e in g])
    g.deleteEdge((1,2))
    print([e for e in g])

    edges = [(1, 5), (1, 3), (1, 7), (5, 2), (5, 3), (3, 4), (3, 6), (2, 4), (2, 6)]
    # you can install this package on your own environment to help understand
    import networkx as nx
    import matplotlib.pyplot as plt
    # visualization
    G = nx.Graph()
    G.add_edges_from(edges)
    print("Print all vertices：{}".format(G.nodes()))
    print("Print all edges：{}".format(G.edges()))
    print("Print the number of edges：{}".format(G.number_of_edges()))
    nx.draw_networkx(G)
    plt.show()

    graph = Graph(edges)
    graph.allDFS()
    for s in graph.vertexList:
        idx = graph.vertexList.index(s)
        print(s,':',[e for e in graph.tree[idx]])

    graph = Graph([ (1,2),(2,4),(3,5),(2,5),(1,5),(3,4),(3,1),(6,2),(6,3),
                    (61, 65), (63, 64), (63, 66), (62, 64), (62, 66)])
    distance,parent = graph.bfs_KD(1)
    print("distance: \t%s\nparent: \t%s" %(distance,parent))
    distance,parent = graph.allBFS()
    print("distance: \t%s\nparent: \t%s" %(distance,parent))
