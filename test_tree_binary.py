from binary_tree import BinaryTree
from binary_tree import BinTreeNode
bt = BinaryTree()

bt.insert(24)
bt.insert(2)
bt.insert(4)
bt.insert(180)
bt.insert(40)
bt.insert(34)
bt.insert(61)

print("in order: ")
bt.in_order_print()

print()

print("reverse order: ")
bt.reverse_order_print()
