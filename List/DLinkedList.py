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
File cs225sp20_env/List/DLinkedList.py
Version 1.2
'''
# %%
class DLinkedList:
    ''' DN<=>A<=>B<=>C<=>D<=> ...<=>Z<=>(back to Dummy Node)'''
    class Node:
        def __init__(self, item, next=None, previous=None):
            self.item = item
            self.next = next
            self.previous = previous

        def __str__(self):
            return str(self.item)

        def __repr__(self):
            return str(self.item)+",pre:"+self.previous.getItem()+",next:"+self.next.getItem()

        def getItem(self):
            return self.item

        def getNext(self):
            return self.next

        def getPrevious(self):
            return self.previous

        def setItem(self, item):
            self.item = item

        def setNext(self, next):
            self.next = next

        def setPrevious(self, previous):
            self.previous = previous

    def __init__(self, contents=[]):
        self.first = DLinkedList.Node(None, None, None)
        self.numItems = 0
        self.first.setNext(self.first)
        self.first.setPrevious(self.first)
        for e in contents:
            self.append(e)

    def __str__(self):
        out_view = []
        cursor = DLinkedList.Node(
            None, self.first.getNext(), self.first.getPrevious())
        for i in range(self.numItems):
            cursor = cursor.getNext()
            out_view.append(cursor.getItem())
        return str(out_view)

    def __getitem__(self, key):
        if key >= 0 and key < self.numItems:
            cursor = self.first.getNext()
            for i in range(key):
                cursor = cursor.getNext()
            return cursor.getItem()
        raise IndexError("DLinkedList index out of range")

    def printList(self):
        tmp = self.first.next
        nodes = []
        for i in range(self.numItems):
            nodes.append(str(tmp.item))
            tmp = tmp.next
        print(' <-> '.join(nodes))

    def count(self, item):
        counter = 0
        cursor = self.first.getNext()
        for i in range(self.numItems):
            if item == cursor.item:
                counter += 1
            cursor = cursor.getNext()
        return counter

    def append(self, item):
        lastNode = self.first.getPrevious()
        newNode = DLinkedList.Node(item, self.first, lastNode)
        lastNode.setNext(newNode)
        self.first.setPrevious(newNode)
        self.numItems += 1

    def delete(self, value):
        cursor = self.first.getNext()
        for i in range(self.numItems):
            if value == cursor.item:
                cursor.getPrevious().setNext(cursor.getNext())
                cursor.getNext().setPrevious(cursor.getPrevious())
                self.numItems -= 1
                return
            cursor = cursor.getNext()
        raise ValueError("DlinkedList does not have this value")

    def locate(self, index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            return cursor
        raise IndexError("DLinkedList index out of range")

    def splice(self, index, other, index1, index2):
        if index1 <= index2:
            begin = other.locate(index1)
            end = other.locate(index2)
            self.insertList(begin, end, index)
            self.numItems += index2-index1+1

    def insertList(self, begin, end, index):
        address = self.locate(index)
        successor = address.getNext()
        begin.setPrevious(address)
        end.setNext(successor)
        address.setNext(begin)
        successor.setPrevious(end)

    def SelectionSort(self):
        firstNode = self.first.getNext()
        lastNode = self.first.getPrevious()
        outlast = self.first
        self.first.setNext(self.first)
        self.first.setPrevious(self.first)
        counter = self.numItems
        while counter != 0:
            location = self.getMinimum(firstNode, lastNode)
            firstNode, lastNode = self.cut(firstNode, lastNode, location)
            # fixed bug: self.addLocation(location)
            outlast = self.addLocation(location, outlast)
            counter -= 1

    def getMinimum(self, first, last):
        minimum = first.getItem()
        cursor = first
        location = first
        while cursor != last:
            cursor = cursor.getNext()
            item = cursor.getItem()
            if item < minimum:
                minimum = item
                location = cursor
        return location

    def cut(self, first, last, location):
        if location == first:
            first = location.getNext()
        else:
            if location == last:
                last = location.getPrevious()
            else:
                prev = location.getPrevious()
                next = location.getNext()
                prev.setNext(next)
                next.setPrevious(prev)
        return first,last

    def addLocation(self, location, outlast):
        location.setPrevious(outlast)
        location.setNext(self.first)
        outlast.setNext(location)
        self.first.setPrevious(location)
        new_outlast = location
        return new_outlast

    def InsertionSort(self):
        cursor = self.first.getNext()
        self.first.setNext(self.first)
        self.first.setPrevious(self.first)
        while cursor != self.first:
            cursor1 = cursor.getNext()         #keep a record of the next cursor position
            self.addout(cursor)
            cursor = cursor1
        
    def addout(self,cursor):
        cursor2 = self.first.getNext()
        while (    cursor2 != self.first\
               and cursor2.getItem() < cursor.getItem()\
               and cursor2.getNext() != self.first):
            # cursor2 is the first node larger than given node  OR  the last node
            cursor2 = cursor2.getNext()

        #insert before cursor2
        if cursor2 != self.first and cursor2.getItem() >= cursor.getItem():
            previous = cursor2.getPrevious()
            previous.setNext(cursor)
            cursor.setNext(cursor2)
            cursor.setPrevious(previous)
            cursor2.setPrevious(cursor)
        #insert at the end of the output
        else:
            cursor2.setNext(cursor)
            cursor.setNext(self.first)
            cursor.setPrevious(cursor2)
            self.first.setPrevious(cursor)

# %%
if __name__ == "__main__":
    l = DLinkedList([124, 134, 5, 6, 23, 4, 5])
    l.printList()
    print(l)

# test splice
    l1 = DLinkedList([1,2,3,4,5,6])
    l2 = DLinkedList([10,20,30,40,50])
    l1.splice(3,l2,1,3)
    print(l1)

# test SelectionSort
    l = DLinkedList([1,2,3,4,5,6,7])
    l.SelectionSort()
    print(l)

    l = DLinkedList([7,6,5,4,3,2,1])
    l.SelectionSort()
    print(l)

    l = DLinkedList([7,6,5,1,2,3,4])
    l.SelectionSort()
    print(l)

# test InsertionSort
    l = DLinkedList([1,2,3,4,5,6,7])
    l.InsertionSort()
    print(l)

    l = DLinkedList([7,6,5,4,3,2,1])
    l.InsertionSort()
    print(l)

    l = DLinkedList([7,6,5,1,2,3,4])
    l.InsertionSort()
    print(l)