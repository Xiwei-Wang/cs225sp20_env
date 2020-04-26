# UIUC CS 225 SP20 ZJUI Environment

This Python package aims to provide the classes used for the UIUC CS 225 SP20 ZJUI Course.

It also aims to build stronger classes via cooperations of students.

**ATTENTION**

**Due to academic integrity, students who will take UIUC CS 225 ZJUI Course taught with Python later than Spring 2020 semester are NOT authorized with the access
to this package!**

Version 1.0

Date 26 April 2020

## Table of Contents
- [UIUC CS 225 SP20 ZJUI Environment](#uiuc-cs-225-sp20-zjui-environment)
  - [Table of Contents](#table-of-contents)
  - [Obtain](#obtain)
  - [Usage](#usage)
  - [Content](#content)
    - [Class](#class)
    - [Demo](#demo)
  - [Dependency](#dependency)
  - [Todo](#todo)
  - [Contributing](#contributing)
    - [Contributers](#contributers)
  - [Update](#update)
  - [License](#license)

## Obtain

In terminal,

```
git clone https://github.com/Xiwei-Wang/cs225sp20_env.git
```

Or fork this repository on the GitHub.

## Usage

In Python,

```
import sys
sys.path.append("path of folder include cs225sp20_env package")
from cs225sp20_env import *
```

In addition,
```
# %%
# %% [markdown]
```
are related with enabling *.py files instead of *.ipynb files calling Jupyter service in VS Code or PyCharm, and we use *.py files because they are much more compatible with git. For more information, you can read the [guide](https://www.notion.so/VScode-python-156cbae7f0134b44a4287459250b27aa) written by Haozhe Chen.

## Content

### Class

* \_\_init__.py <1.0>
* List/
  * \_\_init__.py <1.0>
  * PyList.py <1.0>
  * SPyList.py <1.0>
  * DLinkedList.py <1.0>
  * LinkedList.py <1.0>
  * Fifo.py <1.0>
  * Stack.py <1.0>
* Sort/
  * \_\_init__.py <1.0>
  * selection_sort.py <1.0>
  * bubble_sort.py <1.0>
  * insertion_sort.py <1.0>
  * merge_sort.py <1.0>
* Hash/
  * \_\_init__.py <1.0>
  * HashSet.py <1.0>
  * HashMap.py <1.0>
  * HashSetChaining.py <1.0>
* Tree/
  * \_\_init__.py <1.0>
  * BST.py <1.0>
  * AVLTree.py <1.0>
  * AVLTree_ZZB.py <1.0>
  * FibTree.py <1.0>
  * Trie.py <1.0>
* Graph/
  * \_\_init__.py <1.0>
  * VertexList.py <1.0>
  * EdgeList.py <1.0>
  * Graph.py <1.0> Graph
  * DiGraph.py <1.0> Directed Graph
  * WEdgeList.py <1.0>
  * WGraph.py <1.0> Weighted Graph
  * WDiGraph.py <1.0> Weighted Directed Graph

### Demo

* demo.py <1.0>

## Dependency

* List/
  * SPyList.py <1.0> --> PyList
* Sort/
  * selection_sort.py <1.0> --> PyList, SPyList, DLinkedList, LinkedList
  * bubble_sort.py <1.0> --> PyList, SPyList, DLinkedList, LinkedList
  * insertion_sort.py <1.0> --> PyList, SPyList, DLinkedList, LinkedList
  * merge_sort.py <1.0> --> PyList, SPyList, DLinkedList, LinkedList
* Hash/
  * HashMap.py <1.0> --> HashSet
* Graph/
  * Graph.py <1.0> --> VertexList, EdgeList, PyList, Fifo
  * DiGraph.py <1.0> --> VertexList, EdgeList, PyList, Fifo, Stack
  * WGraph.py <1.0> --> VertexList, WEdgeList, PyList, Fifo
  * WDiGraph.py <1.0> --> VertexList, WEdgeList, PyList, Fifo

## Todo

Generally,
* Add necessary memeber functions to each class
* Add tests
* Add documents

Specifically,
* Make sure all attributes representing data in a class appear in self.\_\_init__(self,...)
* Use inheritance to reduce repetition

## Contributing

Fork at first, then submit pull requrests.

### Contributers

Instructors, TAs and Some Students of UIUC CS 225 SP20 ZJUI Course

* Instructorts
  * Prof. Dr. Klaus-Dieter Schewe

* TAs
  * Tingou Liang
  * Run Zhang
  * Enyi Jiang
  * Xiang Li

* Group 1 Students
   * Shen Zheng
   * Haozhe Chen
   * Ruiqi Li
   * Xiwei Wang
* Other Students
  * Zhongbo Zhu

## Update

* <1.0> - <2020-04-26>
  
For more information, see [ChangeLog.md](./ChangeLog.md)

## License

[MIT © Instructors, TAs and Some Students of UIUC CS 225 SP20 ZJUI Course](./LICENSE)

**ATTENTION**

**Due to academic integrity, students who will take UIUC CS 225 ZJUI Course taught with Python later than Spring 2020 semester are NOT authorized with the access
to this package!**