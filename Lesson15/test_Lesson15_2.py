from Lesson14_1 import *
from Lesson14_2 import *
from Lesson14_3 import *
from binarytree import *

def test_add_lst():
    assert add_lst(t1,ls)==[7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14, -1, 52, 1, 93, 3, 44, None, None, None, None, None, None, None, None, None, None]

def test_search_max():
    assert search_max(t)==62

def test_search_min():
    assert search_min(t)==0

def test_del_under_node():
    assert list(del_unred_node(t1,9).values)==[7, 3, 11, 1, 5, None, 13, 0, 2, 4, 6, None, None, 12, 14]


t = bst(5,is_perfect=True)
ls=[-1, 52, 1, 93, 3, 44]
t1=build([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14])
t2=build([7, 3, 11, 1, 5, None, 13, 0, 2, 4, 6, None, None, 12, 14])




