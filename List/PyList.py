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
File cs225sp20_env/List/PyList.py
Version 1.0
''' 
# %%
class PyList(list):
    def __init__(self,contents=[],size=20):
        self.items = [None] * size
        self.numItems = 0
        self.size = size
        for e in contents:
            self.append(e)
            
    def __contains__(self,item):
        for i in range(self.numItems):
            if self.items[i] == item:
                return True
        return False

    def __eq__(self,other):
        if type(other) != type(self):
            return False
        if self.numItems != other.numItems:
            return False
        for i in range(self.numItems):
            if self.items[i] != self.items[i]:
                return False
        return True

    def __setitem__(self,index,val):
        if index >= 0 and index < self.numItems:
            self.items[index] = val
            return
        raise IndexError("PyList assignment index out of range")

    def __getitem__(self,index):
        if index >= 0 and index < self.numItems:
            return self.items[index]
        raise IndexError("PyList index out of range")

    def __add__(self, other):
        result = PyList(size=self.numItems+other.numItems)
        for i in range(self.numItems):
            result.append(self.items[i])
        for i in range(other.numItems):
            result.append(self.items[i])
        return result

    def __iter__(self):
        for i in self.items:
            if i != None:
                yield i

    def __str__(self):
        return "["+", ".join(str(e) for e in self.items[:self.numItems])+"]"

    def __repr__(self):
        return "PyList(["+", ".join(str(e) for e in self.items[:self.numItems])+"])"

    def list(self):
        return self.items[:self.numItems]

    def index(self, val):
        for i in range(self.numItems):
            if val == self.items[i]:
                return i
        return -1

    def append(self,item):
        if self.numItems == self.size:
            self.allocate()
        self.items[self.numItems] = item
        self.numItems += 1

    def insert(self,i,x):
        if self.numItems == self.size:
            self.allocate()
        if i < self.numItems:
            for j in range(self.numItems-1,i-1,-1):
                self.items[j+1] = self.items[j]
            self.items[i] = x
            self.numItems += 1
        else:
            self.append(x)

    def delete(self,index):
        if self.numItems == self.size / 4:
            self.deallocate()
        if 0 <= index & index < self.numItems:
            for j in range(index, self.numItems-1):
                self.items[j] = self.items[j+1]
            self.numItems -= 1
        else:
            raise IndexError("PyList index out of range")

    def allocate(self):
        newlength = 2 * self.size
        newList = [None] * newlength
        for i in range(self.numItems):
            newList[i] = self.items[i]
        self.items = newList
        self.size = newlength

    def deallocate(self):
        newlength = int(self.size / 2)
        newList = [None] * newlength
        for i in range(self.numItems):
            newList[i] = self.items[i]
        self.items = newList
        self.size = newlength

    def qsort(self):
        if self.numItems <= 1:
            return self
        pivot = self.items[0]
        list1 = PyList([],self.numItems)
        listp = PyList([],self.numItems)
        list2 = PyList([],self.numItems)
        for i in range(self.numItems):
            if self.items[i] < pivot:
                list1.append(self.items[i])
            else:
                if self.items[i] == pivot:
                    listp.append(self.items[i])
                else:
                    list2.append(self.items[i])
        slist1 = list1.qsort()
        slist2 = list2.qsort()
        return (slist1 + listp + slist2)

    def radixSort(self,numdigits,digits):
        sortedlist = self
        for i in range(numdigits):
            sortedlist = sortedlist.Ksort(i,digits)
        return sortedlist          

    def Ksort(self,round,digits):
        bucket = PyList([],digits)
        for k in range(digits):
            newlist = PyList([],self.numItems)
            bucket.append(newlist)
        for i in range(self.numItems):
            item = self.items[i]
            item1 = item // (digits ** round) % digits
            bucket[item1].append(item)
        result = bucket[0]
        for k in range(digits-1):
            result = result + bucket[k+1]

# %%
if __name__ == "__main__":
    l1=PyList([1,2,3])
    print(l1)
    l2=eval(repr(l1))
    print(l2)
    a=l1.list()
    print(a)
