import binarytree
#from binarytree import *

class Tree(binarytree):

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    # Insert method to create nodes
    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    # findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()

    # Added any list - 'ls' to BST - 'tree'
    def add_lst(tree, ls):
        if not tree.is_bst:
            print("This tree is not BST. I can not add list.")
            return None
        else:
            l = list(tree.values)
            h = tree.height
            print(l)
        if not tree.is_perfect:
            col = 2 ** (h + 1) - len(l) - 1
            for i in range(col):
                l.append(None)
        for i in ls:
            l.append(i)
        n = len(l)
        h_new = int(math.log(n + 1, 2) - 1)
        if 2 ** (h_new + 1) - 1 < n:
            h_new += 1
        col = 2 ** (h_new + 1) - len(l) - 1
        for i in range(col):
            l.append(None)

        col1 = (2 ** h_new) - 1
        for i in range(col1):

            if l[i] == None and l[2 * i + 1] == None and l[2 * i + 1] == None:
                continue
            else:

                try:
                    if l[i] < l[2 * i + 1]:
                        print("Значение в списке не соответствует правилам BST. Замените число в списке на значение < ", l[i], end=" ")
                        l[2 * i + 1] = (int(input()))

                    if l[i] > l[2 * i + 2]:
                        print("Значение в списке не соответствует правилам BST. Замените число в списке на значение > ", l[i], end=" ")
                        l[2 * i + 2] = (int(input()))

                except TypeError:
                    continue
        return l


    # Find MAX Node

    def serch_max(self):
        ls = list(self.values)
        if len(ls) == 0:
            print("Такого дерева не існує")
            return None
        elif len(ls) == 1:
            return ls[0]
        elif not self.is_bst:
            print(
                "Функція serch_max може шукати найбільший елемент тільки у BTS. Це дерево не відповідає критеріям BTS ")
            return None
        else:
            i = 1
            max = ls[0]
            while i <= self.height:
                j = int((2 ** (i + 1)) - 2)
                try:
                    if ls[j] > max:
                        max = ls[j]
                except TypeError:
                    return max
                except IndexError:
                    return max
                i += 1
        return max

    # Find MIN Node

    def serch_min(self):
        ls = list(self.values)
        if len(ls) == 0:
            print("Такого дерева не існує")
            return None
        elif len(ls) == 1:
            return ls[0]
        elif not self.is_bst:
            print(
                "Функція serch_max може шукати найбільший елемент тільки у BTS. Це дерево не відповідає критеріям BTS ")
            return None
        else:
            i = 1
            min = ls[0]
            while i <= self.height:
                j = int((2 ** i) - 1)
                try:
                    if ls[j] < min:
                        min = ls[j]
                except TypeError:
                    return min
                except IndexError:
                    return min
                i += 1
        return min

    # Deleted all branches under Node

    def del_unred_node(self, n):
        ls = list(self.values)
        if len(ls) == 0:
            print("Такого дерева не існує")
            return None
        elif len(ls) == 1:
            return None
        elif self.height == 1:
            return None
        elif not self.is_bst:
            print(
                "Функція del_undr_node може шукати найбільший елемент тільки у BTS. Це дерево не відповідає критеріям BTS ")
            return None
        else:
            i = 0
            j = 0
            try:
                while i < self.height or ls[j] != n:
                    jl = 2 * j + 1
                    jr = 2 * j + 2
                    if ls[j] > n:
                        j = jl
                    elif ls[j] < n:
                        j = jr
                    i += 1
            except IndexError:
                print("BTS не містить елементу ", n)
                return self
            else:
                ls[j] = None
                for i in range(j, len(ls)):
                    try:
                        if ls[i] == None:
                            ls[2 * i + 1] = None
                            ls[2 * i + 2] = None
                    except IndexError:
                        continue
                self = build(ls)
        return self

