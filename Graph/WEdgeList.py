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
File cs225sp20_env/Graph/WEdgeList.py
Version 1.0
'''
# %%
class WEdgeList:
    class __Edge:
        def __init__(self, item, weight, next=None, previous=None):
            self.item = item
            self.weight = weight
            self.next = next
            self.previous = previous

        def getItem(self):
            return self.item

        def getWeight(self):
            return self.weight

        def getNext(self):
            return self.next

        def getPrevious(self):
            return self.previous

        def setItem(self, item):
            self.item = item

        def setWeight(self, weight):
            self.weight = weight

        def setNext(self, next):
            self.next = next

        def setPrevious(self, previous):
            self.previous = previous

    def __init__(self, edge, weight):
        self.first = WEdgeList.__Edge(edge, weight, None, None)
        self.first.setNext(self.first)
        self.first.setPrevious(self.first)
        self.numEdges = 1

    def add(self, edge, weight):
        lastEdge = self.first.getPrevious()
        newEdge = WEdgeList.__Edge(edge, weight, self.first, lastEdge)
        lastEdge.setNext(newEdge)
        self.first.setPrevious(newEdge)
        self.numEdges += 1

    def locate(self, item):
        cursor = self.first
        for i in range(self.numEdges):
            cursor = cursor.getNext()
            if item == cursor.getItem():
                return cursor

    def __iter__(self):
        cursor = self.first
        for i in range(self.numEdges):
            yield (cursor.getItem(), cursor.getWeight())
            cursor = cursor.getNext()

    def __contains__(self, item):
        cursor = self.first
        for i in range(self.numEdges):
            vertex = cursor.getItem()
            if vertex == item:
                return True
            cursor = cursor.getNext()
        return False

    def remove(self, item):
        cursor = self.first
        for i in range(self.numEdges):
            vertex = cursor.getItem()
            if vertex == item:
                nextVertex = cursor.getNext()
                prevVertex = cursor.getPrevious()
                prevVertex.setNext(nextVertex)
                nextVertex.setPrevious(prevVertex)
                self.numEdges -= 1
                if (cursor == self.first):
                    self.first = nextVertex
                return True
            cursor = cursor.getNext()
        return False