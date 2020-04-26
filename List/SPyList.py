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
File cs225sp20_env/List/SPyList.py
Version 1.0
'''
# %%
# for VS Code users
if __name__ != "cs225sp20_env.List.SPyList":
    import sys
    sys.path.append(__file__[:-len("cs225sp20_env/List/SPyList.py")])
# %%cs225sp20-env
# for PyCharm users
if __name__ != "cs225sp20_env.List.SPyList":
    import sys
    import os
    sys.path.append(os.getcwd())
# %%
from cs225sp20_env.List.PyList import PyList
# %%
class SPyList(PyList):
    def __init__(self, contents=[], size=10):
        self.items = [None] * size
        self.keys = []  # modification
        self.numItems = 0
        self.size = size
        for e in contents:
            self.append(e)

    def append(self, item):
        if (type(item) is not dict):
            raise TypeError("Wrong Element Tpye, dict Type Expected")
        if (item['key'] in self.keys):  # modification
            raise KeyError("Key already exists")
        if self.numItems == self.size:
            self.allocate()
        self.items[self.numItems] = item
        self.numItems += 1
        self.keys.append(item['key'])  # modification

    def __setitem__(self, index, val):
        if (type(val) is not dict):
            raise TypeError("Wrong Element Tpye, dict Type Expected")
        if index >= 0 and index < self.numItems:
            old_key = self.items[index]['key']  # modification
            if(val['key'] != old_key and val['key'] in self.keys):
                raise KeyError("Key already exists")
            self.keys.remove(old_key)
            self.keys.append(val['key'])
            self.items[index] = val
            return
        raise IndexError("PyList assignment index out of range")

    def __add__(self, other):
        raise SyntaxError("Add operation not defined")  # modification

    def insert(self, i, x):
        if(type(x) is not dict):
            raise TypeError("Wrong Element Tpye, dict Type Expected")
        if (x['key'] in self.keys):  # modification
            raise KeyError("Key already exists")
        if self.numItems == self.size:
            self.allocate()
        if i < self.numItems:
            for j in range(self.numItems-1, i-1, -1):
                self.items[j+1] = self.items[j]
            self.items[i] = x
            self.numItems += 1
            self.keys.append(x['key'])
        else:
            self.append(x)

    def projection(self, projectList):
        newContent = []
        for item in self.items:
            if (item == None):
                continue
            newItem = {}
            for key in item.keys():
                if (key in projectList):
                    newItem[key] = item[key]
            newContent.append(newItem)
        return PyList(newContent)

    def projection_m(self, projectList):
        newContent = []
        for item in self.items:
            if (item == None):
                continue
            newItem = {}
            for key in item.keys():
                if (key in projectList):
                    newItem[key] = item[key]
            newContent.append(newItem)
        # If there are duplicated elements, raise an error
        for i in range(len(newContent) - 1):
            if (newContent[i] in newContent[i+1:]):
                raise ValueError("Duplicated records after projection")
        return PyList(newContent)

# %%
if __name__ == "__main__":
    slist = SPyList([
        {"key": 0, "name": "Toom", "state": "student", "age": 18, "score": 98},
        {"key": 1, "name": "Annn", "state": "student", "age": 19, "score": 80},
        {"key": 2, "name": "Giao", "state": "student", "age": 24, "score": 7},
        {"key": 3, "name": "FFck", "state": "teacher",
         "age": 79, "payment": 800},
        {"key": 4, "name": "Kela", "state": "teacher",
         "age": 33, "payment": 999},
    ])

    slist.append({"key": 5, "name": "Mono",
                  "state": "student", "age": 23, "score": 13},)
    slist[0] = {"key": 0, "name": "Sabi",
                "state": "student", "age": 18, "score": 98}
    slist.insert(2, {"key": 7, "name": "Kela",
                     "state": "teacher", "age": 33, "payment": 999})
    names = slist.projection(["name"])
    age_and_score = slist.projection(["age", "score"])
    try:
        states = slist.projection_m(["state"])
    except:
        pass
