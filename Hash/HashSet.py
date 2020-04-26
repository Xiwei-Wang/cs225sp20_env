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
File cs225sp20_env/Hash/HashSet.py
Version 1.0
'''
# %%
class HashSet:
    class __Placeholder:
        def __init__(self):
            pass

        def __eq__(self, other):
            return False

    def __init__(self, contents=[]):
        self.items = [None] * 10
        self.numItems = 0

        for e in contents:
            self.add(e)

    def __iter__(self):
        for i in self.items:
            if i != None and type(i) != HashSet.__Placeholder:
                yield i

    def __contains__(self, item):
        index = hash(item) % len(self.items)
        # theoritically, index = hash(item) and modulus is included in hash()
        # technically, we use Python built-in function hash()
        while self.items[index] != None:
            if self.items[index] == item:
                return True
            index = (index + 1) % len(self.items)
        return False

    def add(self, item):
        if self.__add(item, self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = self.__rehash(self.items, [None] * 2 * len(self.items))

    def __add(self, item, items):
        index = hash(item) % len(items)
        location = -1
        while items[index] != None:
            if items[index] == item:
                return False
            if location < 0 and type(items[index]) == HashSet.__Placeholder:
                location = index
            index = (index + 1) % len(items)
        if location < 0:
            location = index
        items[location] = item
        return True

    def __rehash(self, olditems, newitems):
        for e in olditems:
            if e != None and type(e) != HashSet.__Placeholder:
                self.__add(e, newitems)
        return newitems

    def delete(self, item):
        if self.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 20) / len(self.items)
            if load <= 0.25:
                self.items = self.__rehash(self.items, [None] * (len(self.items) // 2))
        else:
            raise KeyError("Item not in HashSet")

    def __remove(self, item, items):
        index = hash(item) % len(items)
        while items[index] != None:
            if items[index] == item:
                nextIndex = (index + 1) % len(items)
                if items[nextIndex] == None:
                    items[index] = None
                else:
                    items[index] = HashSet.__Placeholder()
                return True
            index = (index + 1) % len(items)
        return False
# %%
if __name__ == "__main__":
    import random

    # explictly test
    M = HashSet()
    operates = ["find", "insert", "delete"]
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # add
    for num in num_list:
        M.add(num)

    # find
    for num in num_list:
        if num in M:
            pass
        else:
            print("not find exist element")
    if 11 in M:
        print("find wrong element")

    # delete
    for num in num_list:
        M.delete(num)

    for num in num_list:
        try:
            M.delete(num)
        except:
            pass
        else:
            print("find wrong element")

    # test with large data and check with build in class
    M = HashSet()
    operates = ["find", "insert", "delete"]
    num_list = list(range(1000))
    recorder = set()

    for i in range(5000):
        operate = random.choice(operates)
        num = random.choice(num_list)
        if operate == "insert":
            M.add(num)
            recorder.add(num)
        elif operate == "find":
            if num in M:
                if num in recorder:
                    pass
                else:
                    print("fail to delete")
            else:
                if num in recorder:
                    print("fail to insert")
        elif operate == "delete":
            if num in M:
                M.delete(num)
                recorder.remove(num)
