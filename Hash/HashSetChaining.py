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
File cs225sp20_env/Hash/HashSetChaining.py
Version 1.0
'''
# %%
class HashSetChaining:
    def __init__(self,contents=[],loadMax=0.75,loadMin=0.25):
        self.items = [None] * 20
        self.numItems = 0
        self.loadMax = loadMax
        self.loadMin = loadMin
        for e in contents:
            self.add(e)
            
    def add(self,item):
        if HashSetChaining.__add(item,self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= self.loadMax:
                self.items = HashSetChaining.__rehash(self.items, [None]*2*len(self.items))
                
    def __contains__(self,item):
        index = hash(item) % len(self.items)
        if self.items[index] == None or type(self.items[index]) == HashSetChaining.__Placeholder:
            return False
        if item in self.items[index]:
            return True
        return False
    
    def delete(self,item):
        if HashSetChaining.__remove(item,self.items):
            self.numItems -= 1
            load = max(self.numItems,20) / len(self.items)
            if load <= self.loadMin:
                self.items = HashSetChaining.__rehash(self.items, [None]*(len(self.items) // 2))
        else:
            raise KeyError("Item not in HashSet")

    # ===== Hidden Class =====
    class __Placeholder:
        def __init__(self):
            pass
        
        def __eq__(self,other):
            return False
    
    # ===== Auxiliary Functions =====
    # They all have '__' as prefixes to indicate that they are private methods to the class
    def __add(item,items):
        index = hash(item) % len(items)
        if items[index] == None:
            items[index] = []
        if item in items[index]:
            return False
        items[index].append(item)
        return True
        
    def __rehash(olditems,newitems):
        for chain in olditems:
            if chain != None and type(chain) != HashSetChaining.__Placeholder:
                for e in chain:
                    HashSetChaining.__add(e,newitems)
        return newitems
                
    def __remove(item,items):
        index = hash(item) % len(items)
        if item in items[index]:
            items[index].remove(item)
            # If the list is empty, replace it with a placeholder
            if items[index] == []:
                items[index] = HashSetChaining.__Placeholder()
            return True
        return False
