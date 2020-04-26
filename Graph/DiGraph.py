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
File cs225sp20_env/Graph/DiGraph.py
Version 1.0
'''
# %%
# for VS Code users
if __name__ != "cs225sp20_env.Graph.DiGraph":
    import sys
    sys.path.append(__file__[:-len("cs225sp20_env/Graph/DiGraph.py")])
# %%
# for PyCharm users
if __name__ != "cs225sp20_env.Graph.DiGraph":
    import sys
    import os
    sys.path.append(os.getcwd())
# %%
from cs225sp20_env.Graph.VertexList import VertexList
from cs225sp20_env.Graph.EdgeList import EdgeList
from cs225sp20_env.List.PyList import PyList
from cs225sp20_env.List.Fifo import Fifo
from cs225sp20_env.List.Stack import Stack
# %%
class DiGraph:
    def __init__(self,edges=[]):
        self.vertexList = VertexList(edges)
        for e in edges:
            self.addEdge(e)
            ## Modification
            # for directed graph, we only need to store one direction - (in, out)
            # self.addEdge((e[1],e[0])) 

    def addEdge(self,edge):
        # locate the related vertex according to the edge given
        vertex = self.vertexList.locate(edge[0]) # edge[0] is the incoming vertex
        edgelist = vertex.edges # get the edgelist object for this incoming vertex
        if edgelist != None:
            # add outcoming vertex to the edgelist
            edgelist.add(edge[1])
        else:
            # construct a new Edgelist object if this vertex has no edgelist yet
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
        ## Modification, only one direction now
        # self.addEdge((edge[1],edge[0]))

    def deleteEdge(self,edge):
        self.__deleteEdge(edge)
        ## Modification, only one direction now
        # self.__deleteEdge((edge[1],edge[0]))

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

    def bfs(self,vertex):
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
                print(u)
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

    #DFS traverse using recursion
    def allDFS(self):
        numVertices = self.vertexList.getlength()
        initlist = [None]* numVertices
        self.tree = PyList(initlist,numVertices)
        for i in range(numVertices):
            newgraph = DiGraph([])
            self.tree[i] = newgraph
        for s in self.vertexList:
            self.mark = [None] * numVertices
            self.dfsPos = 1
            self.dfsNum = [1] * numVertices
            self.finishingTime = 1
            self.finishTime = [1] * numVertices
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

    def reachable(self,vertex1,vertex2):
        ret=self.bfs_for_path(vertex1)
        distance=ret[0]
        parent=ret[1]
        loc = self.vertexList.index(vertex2)
        if parent[loc]==None:
            return False
        else:
            return True

    def path(self,vertex1,vertex2):
        ret=self.bfs_for_path(vertex1)
        distance=ret[0]
        parent=ret[1]
        loc = self.vertexList.index(vertex2)
        if parent[loc]==None:
            return None
        p=parent[loc]
        c=vertex2
        path=PyList()
        while p!=vertex1:
            loc = self.vertexList.index(c)
            p=parent[loc]
            path.insert(0,(p,c))
            c=p
        path.append((p,c))
        return path

    def bfs_for_path(self,vertex):
        if not (vertex in self.vertexList):
            print("There is no vertex", vertex)
            return None
        length = self.vertexList.getlength()
        distance = [None] * length
        parent = [None] * length
        index = self.vertexList.index(vertex)
        distance[index] = 0
        parent[index] = vertex
        queue = Fifo(length)
        queue.pushback(vertex)
        for l in range(length):
            for u in queue:
                # print(u)
                loc = self.vertexList.locate(u)
                edgelist = loc.getEdges()
                if edgelist != None:
                    for v in edgelist:
                        idx = self.vertexList.index(v)
                        if parent[idx] == None:
                            queue.pushback(v)
                            distance[idx] = l + 1
                            parent[idx] = u
        return (distance,parent)
