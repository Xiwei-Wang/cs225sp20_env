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
File cs225sp20_env/Tree/AVLTree_ZZB.py
Version 1.0
'''
# %%
class AVLTree_ZZB:
    class AVLNode:
        def __init__(self, item, height=0, left=None, right=None):
            self.item = item
            self.height = height
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
            yield self.item, self.height
            if self.right != None:
                for elem in self.right:
                    yield elem

    def __init__(self):
        self.root = None

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    @staticmethod
    def __rotateLeft(tree, parent, node, direction):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        if direction == 1:
            parent.right = new_root
        elif direction == -1:
            parent.left = new_root
        else:
            assert(direction == 0)
            tree.root = new_root

    @staticmethod
    def __rotateRight(tree, parent, node, direction):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        if direction == 1:
            parent.right = new_root
        elif direction == -1:
            parent.left = new_root
        else:
            assert(direction == 0)
            tree.root = new_root
        return

    @staticmethod
    def __rotateRightLeft(tree, parent, node, direction):
        AVLTree_ZZB.__rotateRight(tree, node, node.right, 1)
        AVLTree_ZZB.__rotateLeft(tree, parent, node, direction)
        return

    @staticmethod
    def __rotateLeftRight(tree, parent, node, direction):
        AVLTree_ZZB.__rotateLeft(tree, node, node.left, -1)
        AVLTree_ZZB.__rotateRight(tree, parent, node, direction)
        return

    def insert(self, item):
        self.__insert(self, self.root, None, item)

    @staticmethod
    def __insert(tree, node, parent, item, direction=0):
        if node is None:
            if direction == 1:
                node = AVLTree_ZZB.AVLNode(item)
                parent.right = node
            elif direction == 0:
                node = AVLTree_ZZB.AVLNode(item)
                tree.root = node
            else:
                node = AVLTree_ZZB.AVLNode(item)
                parent.left = node
        elif item < node.item:
            AVLTree_ZZB.__insert(tree, node.left, node, item, -1)
            AVLTree_ZZB.rebalance(tree, parent, node, direction)
        elif item > node.item:
            AVLTree_ZZB.__insert(tree, node.right, node, item, 1)
            AVLTree_ZZB.rebalance(tree, parent, node, direction)
        node.height = max(AVLTree_ZZB.get_height(node.left), AVLTree_ZZB.get_height(node.right))+1

    @staticmethod
    def rebalance(tree, parent, node, direction):
        difference = AVLTree_ZZB.get_height(node.left) - AVLTree_ZZB.get_height(node.right)
        if 1 >= difference >= -1:
            return
        elif difference>=2:
            # the left is higher
            if AVLTree_ZZB.get_height(node.left.left) > AVLTree_ZZB.get_height(node.left.right):
                AVLTree_ZZB.__rotateRight(tree, parent, node, direction)
            else:
                AVLTree_ZZB.__rotateLeftRight(tree, parent, node, direction)
        elif difference<=-2:
            if AVLTree_ZZB.get_height(node.right.right) > AVLTree_ZZB.get_height(node.right.left):
                AVLTree_ZZB.__rotateLeft(tree, parent, node, direction)
            else:
                AVLTree_ZZB.__rotateRightLeft(tree, parent, node, direction)
        node.height = max(AVLTree_ZZB.get_height(node.left), AVLTree_ZZB.get_height(node.right))+1

    @staticmethod
    def get_height(node):
        if node is None:
            return -1
        return node.height

    def find(self, item):
        def __find(root, item):
            if root == None:
                return False
            if item == root.item:
                return True
            if item < root.item:
                return __find(root.left, item)
            else:
                return __find(root.right, item)
        return __find(self.root, item)

    def delete(self, item):
        self.__delete(self, self.root, None, item)

    @staticmethod
    def __delete(tree, node, parent, item, direction=0):
        def helper(parent, node, direction):
            if direction == 1:
                parent.right = node
            elif direction == -1:
                parent.left = node
            else:
                tree.root = node
        if node is None:
            return
        if item < node.item:
            AVLTree_ZZB.__delete(tree, node.left, node, item,  -1)
            AVLTree_ZZB.rebalance(tree, parent, node, direction)
        elif item > node.item:
            AVLTree_ZZB.__delete(tree, node.right, node, item, 1)
            AVLTree_ZZB.rebalance(tree, parent, node, direction)
        elif item == node.item:
            # the core part of the delete
            if node.right is None and node.left is None:
                # leaf's deletion
                helper(parent, None, direction)
                node = None
            elif node.right is not None and node.left is not None:
                # two child deletion
                temp = node.left
                while temp.right is not None:
                    temp = temp.right
                node.item = temp.item
                AVLTree_ZZB.__delete(tree, node.left, node, node.item, -1)
                AVLTree_ZZB.rebalance(tree, parent, node, direction)
            else:
                # one child's deletion
                if node.left is None:
                    node = node.right
                    helper(parent, node, direction)
                else:
                    node = node.left
                    helper(parent, node, direction)
        if node is None:
            return
        AVLTree_ZZB.rebalance(tree, parent, node, direction)
        return
# %%
if __name__ == "__main__":
    avl = AVLTree_ZZB()
    content = [12,7,19,14,13,21,23]
    for i in content:
        avl.insert(i)
    for i in avl:
        print(i)
    print("-----")
    avl.delete(21)
    avl.delete(12)
    for i in avl:
        print(i)
