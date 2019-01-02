class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class BinaryTree:
	def __init__(self, node):
		self.root = TreeNode(node)

	def get_node(self, root, x):
		if root.val == x:
			return root
		if root.left:
			return self.get_node(root.left, x)
		if root.right:
			return self.get_node(root.right, x)

	def traversal(self, root):
		res = []
		if root:
			res = self.traversal(root.left)
			res = res + self.traversal(root.right)
			res.append(root.val)
		return res

def add_one(root):
	if not root:
		return root
	else:
		root.val += 1
	if root.left:
		return add_one(root.left)
	if root.right:
		return add_one(root.right)


def merge(t1, t2):
	if t1 and t2:
		t1.val += t2.val
	elif not t1 and t2:
		return t2
	elif t1 and not t2:
		return t1
	elif not t1 and not t2:
		return None
	t1.left = merge(t1.left, t2.left)
	t1.right = merge(t1.right, t2.right)
	return t1


def iterate(root):
	stack = [root]
	current = stack[0]
	while stack and current:
		if current.left:
			current = current.left
			stack.append(current)
		if not current.left and stack:
			item = stack.pop()
			if item.right:
					current = item.right
					stack.append(current)
			print(item.val)


def main():
	#[1,3,2,5]
	#[2,1,3,null,4,null,7]
	t1 = BinaryTree(1)
	t1.root.left = TreeNode(3)
	t1.root.right = TreeNode(2)
	t1.root.left.left = TreeNode(5)

	#iterate(t1.root)

	#root = add_one(t1.root)
	#print(t1.traversal(t1.root))

	t2 = BinaryTree(2)
	t2.root.left = TreeNode(1)
	t2.root.right = TreeNode(3)
	t2.root.right.right = TreeNode(3)
	t2.root.left.right = TreeNode(1)
	t2.root.left.left = TreeNode(1)

	#print(t2.traversal(t2.root))
	#merge(t1.root, t2.root)
	print(t2.traversal(t2.root))


if __name__ == '__main__':
	main()
