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
File cs225sp20_env/Tree/BST.py
Version 1.0
'''
# %%
class BST:
    class __Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right
            self.parent = None

        def getVal(self):
            return self.val

        def setVal(self,newval):
            self.val = newval

        def getLeft(self):
            return self.left

        def setLeft(self,newleft):
            self.left = newleft

        def getRight(self):
            return self.right

        def setRight(self,newright):
            self.right = newright 

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
            yield self.val
            if self.right != None:
                for elem in self.right:
                    yield elem
                    
    def __init__(self):
        self.root = None

    def insert(self,val):
        def __insert(root,val):
            if root == None:
                return BST.__Node(val)
            if val < root.getVal():
                root.setLeft(__insert(root.getLeft(),val))
            else:
                root.setRight(__insert(root.getRight(),val))
            return root
        self.root = __insert(self.root,val)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    def find(self,val):
        def __find(root,val):
            if root == None:
                return False
            if val == root.getVal():
                return True
            if val < root.getVal():
                return __find(root.getLeft(),val)
            else:
                return __find(root.getRight(),val)
        return __find(self.root,val)

    #FIXME: if the deleted node is root,the tree won't change
    def delete(self,val):
        def __merge(leftnode,rightnode):
            if rightnode == None:
                return leftnode
            elif rightnode.getLeft() == None:
                rightnode.setLeft(leftnode)
                return rightnode
            else:
                __merge(leftnode,rightnode.getLeft())
                return rightnode
        def __delete(root,val):
            if root == None:
                # the case that val is not in BST
                print(str(val),"is not in the BST")
                return root
            if val == root.getVal():
                return __merge(root.getLeft(),root.getRight())
            elif val < root.getVal():
                root.setLeft(__delete(root.getLeft(),val))
                return root
            else:
                root.setRight(__delete(root.getRight(),val))
                return root

        if val == self.root.getVal():
            self.root = __delete(self.root,val)
            self.root.parent = None # NOTE: the memory has not been freed
        else:
            __delete(self.root,val)

    ## Add a function to print out the tree intuitionistically
    def print_BST(self):
        print('-'*100)
        ret = self.print_tree(self.root, 0, 0,{})
        ret = sorted(ret.items(), key=lambda x: x[1])
        cur_x = 0
        cur_y = 0
        for item in ret:
            x = item[1][1]
            y = item[1][0]
            parent = item[1][2]
            for i in range(cur_y, y):
                print('\n')
                cur_x = 0
            for i in range(cur_x, x):
                print(' ', end='')
            print(item[0], end='')
            print('('+str(parent)+')',end = '')
            cur_x = x+1
            cur_y = y
        # print('\n')
        print('')
        print('-'*100)
        
    # helper function
    def print_tree(self, root, x, y, ret):
        # none do nothing and return
        if(root == None):
            return ret
        if(root.left == None and root.right == None): # leaf node   
            ret[str(root.val)] = (y, x, root.parent.val)
            return ret
        # otherwise, the left or right node is not None
        if(x-8 < 0):
            x = 8
        if(root.left != None):
            root.left.parent = root
            ret = self.print_tree(root.left, x-8, y+1, ret)
            leftChild = str(root.left.val)
            if(root == self.root):
                x = ret[leftChild][1]+16 # to distinct left and right tree
            else:
                x = ret[leftChild][1]+8
        if(root.parent == None):
            ret[str(root.val)] = (y, x, None)
        else:
            ret[str(root.val)] = (y, x, root.parent.val)
        if(root.right != None):
            root.right.parent = root
            if(root == self.root):
                ret = self.print_tree(root.right, x+16, y+1, ret) # to distinct left and right tree
            else:
                ret = self.print_tree(root.right, x+8, y+1, ret)
        return ret
# %%
if __name__ == "__main__":
    import random
    # manual test
    bst = BST()
    lst = [3, 8, 9, 2, 4, 0, 6, 5, 1, 7]
    print(lst)
    for i in lst:
        bst.insert(i)

    bst_lst = [elem for elem in bst]
    print(bst_lst)
    bst.print_BST()

    bst.delete(3)
    bst_lst = [elem for elem in bst]
    print(bst_lst)
    bst.print_BST()

    bst.delete(3)

    print(bst.find(1))
    print(bst.find(3))

    # random test
    bst = BST()
    lst = [i for i in range(1000)]
    random.shuffle(lst)
    for i in lst:
        bst.insert(i)

    lst = [i for i in range(500)]
    random.shuffle(lst)
    for i in lst:
        before_del_root = bst.root.getVal()
        bst.delete(i)
        assert i not in bst 

    lst = [i for i in range(500,1000)]
    random.shuffle(lst)
    for i in lst:
        assert bst.find(i)

    lst = [i for i in range(500)]
    random.shuffle(lst)
    for i in lst:
        assert not bst.find(i) 
