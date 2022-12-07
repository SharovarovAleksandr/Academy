from binarytree import *
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


    def add_lst(self,tree,ls):
        if not tree.is_bst:
            print("This tree is not BST. I can not add list.")
        else:
        l = list(tree.values)
        h = tree.height
        if tree.is_perfect:
            for i in ls:
                l1.append(i)
        else:
            if len(l)<2**(h-1):
                for i in range(len(l),2**(h-1)+1):
                    l.append(None)
        print(l)




    def inp(n):
        while True:
            print("Enter number less then", n, end="  ")
            l = input()
            if l == "":
                l = None
                break
            else:
                l = int(l)
                if l > n:
                    print("Number more then", n)
                else:
                    break
        while True:
            print("Enter number more then", n, end="  ")
            r = input()
            if r == "":
                r = None
                break
            else:
                r = int(r)
                if r < n:
                    print("Number less then", n)
                else:
                    break
        return l, r

    def gen_tr(h, r, aut):
        j = 1
        while j < h + 1:
            st = int(2 ** (j - 1) - 1)
            en = int(2 ** j - 1)
            for i in range(st, en):
                if ls[i] == None:
                    ls.append(None)
                    ls.append(None)
                else:
                    if aut == "Y":
                        a, b = inp_rand(ls[i], max)
                        ls.append(a)
                        ls.append(b)
                    else:
                        a, b = inp(ls[i])
                        ls.append(a)
                        ls.append(b)
            j += 1
        return ls