class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def printInorder( node):
	if node:
		printInorder(node.left)
		print(node.val)
		printInorder(node.right)

def printPreOrder(node):
	if node:
		print(node.val)
		printPreOrder(node.left)
		printPreOrder(node.right)

def printPostOrder(node):
	if node:
		printPostOrder(node.left)
		printPostOrder(node.right)
		print(node.val)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("In Order: ")
print(printInorder(root))
print("PreOrder: ")
print(printPreOrder(root))
print("PostOrder: ")
print(printPostOrder(root))


