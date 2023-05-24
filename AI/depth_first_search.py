class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node):
    if not node:
        return

    # Process node (print value, perform some operation, etc.)
    print(node.val)

    dfs(node.left)
    dfs(node.right) 

# Example usage
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Perform DFS on the tree
dfs(root)

#output-1 2 4 5 3 6 7
