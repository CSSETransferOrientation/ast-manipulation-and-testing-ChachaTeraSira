#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Operating on lists, that's a python builtin

def my_sum_list(l):
    """
    Take in a list of numbers, and return their sum
    """
    s = 0
    for n in l:
        s += n
    return s


# In[ ]:


t0 = [1]
t1 = [-1]
t2 = []
t3 = [1, 2, 3]


# In[ ]:


assert True == True


# In[ ]:


assert True == False


# In[ ]:


assert my_sum_list(t0) == 1
assert my_sum_list(t1) == -2
assert my_sum_list(t2) == 1
assert my_sum_list(t3) == 6


# In[ ]:


import unittest


# In[ ]:


class ListTester(unittest.TestCase):
    def test_hereprint(self):
        print("Hello")
        
    def test_long(self):
        self.test_hereprint()
        self.assertEqual(my_sum_list([1, 2, 3, 4, 5]),
                         15)
    def test_empty(self):
        self.assertEqual(my_sum_list([]),
                 0)
    def test_fail(self):
        self.assertEqual(my_sum_list([1]),
                 1)       


# In[ ]:


unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:


def recur_sum(l):
    """
    Add elements of a list recursively
    """
    if not l:
        return 0
    else:
        return l[0] + recur_sum(l[1:])


# In[ ]:


class RecurTester(unittest.TestCase):      
    def test_long(self):
        self.assertEqual(recur_sum([1, 2, 3, 4, 5]),
                         15)
    def test_empty(self):
        self.assertEqual(recur_sum([]),
                 0)
    def test_fail(self):
        self.assertEqual(recur_sum([1]),
                 1)


# In[ ]:


unittest.main(argv=[''], verbosity=2, exit=False)


# %pip install binarytree

# In[ ]:


import binarytree


# In[ ]:


l = [1, 2, 3, 4, 5]
t = binarytree.build(l)
print(t)


# In[ ]:


# data is binary tree of numbers


# In[ ]:


t1 = binarytree.build([1])


# In[ ]:


print(t1)


# In[ ]:


if t1:
    print("yes")
else:
    print("no")


# In[ ]:


def sum_binary_tree(t):
    """
    Walk the tree, find the sum of all elements
    """
    if not t:
        return 0
    return t.val + sum_binary_tree(t.left) + sum_binary_tree(t.right)


# In[ ]:


t1 = binarytree.build([])
assert sum_binary_tree(t1) == 0

t2 = binarytree.build([1,2,3,4,5])
assert sum_binary_tree(t2) == 15


# In[ ]:


sum_binary_tree(t2)


# In[ ]:


from os.path import join as osjoin
import os


# In[ ]:


os.getcwd()


# In[ ]:


os.listdir()


# In[ ]:


'binary_tree_files\inputs'
'binary_tree_files/inputs'


# In[ ]:


ins = osjoin('binary_tree_files', 'inputs')
outs = osjoin('binary_tree_files', 'outputs')
for dirpath, dirnames, filenames in os.walk(ins):
    for fname in filenames:
        print(f'testing {fname}')
        with open(osjoin(ins, fname)) as f:
            inp = f.read().strip()
        with open(osjoin(outs, fname)) as f:
            expected = int(f.read().strip())
        t = binarytree.build([int(i) for i in inp.split()])
        out = sum_binary_tree(t)
        assert out == expected


# In[ ]:


class BinTreeSumTester(unittest.TestCase):
    ins = osjoin('binary_tree_files', 'inputs')
    outs = osjoin('binary_tree_files', 'outputs')
    def test_all_the_things(self):
        for fname in os.listdir(ins):
            with open(osjoin(ins, fname)) as f:
                inp = f.read().strip()
            with open(osjoin(outs, fname)) as f:
                expected = int(f.read().strip())
                with self.subTest(msg=f"Testing {fname}", inp=inp, expected=expected):
                    t = binarytree.build([int(i) for i in inp.split()])
                    out = sum_binary_tree(t)
                    self.assertEqual(out, expected)


# In[ ]:


unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




