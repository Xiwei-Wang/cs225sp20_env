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
File cs225sp20_env/Tree/Trie.py
Version 1.0
'''
# %%
class Trie:
    class TrieNode:
        def __init__(self,item,next=None,follows=None): 
            self.item = item
            self.next = next
            self.follows = follows 
    
    def __init__(self):
        self.start = None 
    
    def insert(self,item):
        if type(item) == str: item = list(item)
        self.start = Trie.__insert(self.start,item)
    
    def __contains__(self,item):
        if type(item) == str: item = list(item)
        return Trie.__contains(self.start,item+["#"])
    
    def __insert(node,item): 
        if item == []:  # end condition
            if node != None:
                newnode = Trie.TrieNode('#',next=node)
            else:
                newnode = Trie.TrieNode("#")
            return newnode

        if node == None:    # if trie is empty
            key = item.pop(0) # one letter per node 
            newnode = Trie.TrieNode(key)
            newnode.follows = Trie.__insert(newnode.follows,item) 
            return newnode
        else:
            key = item[0]
            if node.item == key:    # letter already in the trie
                key = item.pop(0)
                node.follows = Trie.__insert(node.follows,item)
            else:
                node.next = Trie.__insert(node.next,item)
            return node
    
    def __contains(node,item): 
        if type(item) == str: item = list(item)
        if item == []:
            return True
        if node == None:
            return False
        key = item[0]
        if node.item == key:
            key = item.pop(0)
            return Trie.__contains(node.follows,item)
        return Trie.__contains(node.next,item)

    # a print function which can print out structure of tries 
    # to help better understand
    def print_trie(self,show_start = False):
        if show_start:
            print('start\n   |\n   ',end='')
            self.__print_trie(self.start,1)
        else:
            self.__print_trie(self.start,0)

    def __print_trie(self, root, level_f):
        if(root == None):
            return
        if(root.item != '#'):
            print(root.item, '-', end='')
        else:
            # print(root.item, end='')  # modified
            print(root.item, end='\n')  
        self.__print_trie(root.follows, level_f+1)
        if(root.next!=None):
            # print('\n') # commented
            str_sp = ' '*level_f*3 
            print(str_sp+'|')
            print(str_sp, end='')
        self.__print_trie(root.next,level_f)
        return
# %%
if __name__ == '__main__':
    trie = Trie()
    for word in [   'cow','cowboy',
                    'cat','rat','rabbit','dog',
                    'pear','peer','pier']:
        trie.insert(word)
    assert 'cow' in trie
    assert 'cowboy' in trie
    assert 'pear' in trie
    assert 'peer' in trie
    assert 'pier' in trie
    trie.print_trie()
