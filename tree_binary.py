class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root
    
    def _insert(self, root, new_item):
        if(root.data > new_item):
            if(root.left != None):
                self._insert(root.left, new_item)
            else:
                root.left = BinTreeNode(new_item)
        else:
            if(root.right != None):
                self._insert(root.right, new_item)
            else:
                root.right = BinTreeNode(new_item)

    def insert(self, new_item):
        if(self.root != None):
            self._insert(self.root, new_item)
        else:
            self.root = BinTreeNode(new_item)

    def _in_order_print(self, node):
        if(node != None):
            self._in_order_print(node.left)
            print(node)
            self._in_order_print(node.right)

    def in_order_print(self):
        if(self.root == None):
            print("Tree is empty")
        else:
            self._in_order_print(self.root)

    def _reverse_order_print(self, node):
        if(node != None):
            self._reverse_order_print(node.right)
            print(node)
            self._reverse_order_print(node.left)

    def reverse_order_print(self):
        if(self.root == None):
            print("Tree is empty")
        else:
            self._reverse_order_print(self.root)


class BinTreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return "{}\tleft:\t{}\tright: {}".format(self.data, (self.left.data if self.left else "-"), (self.right.data if self.right else "-"))
