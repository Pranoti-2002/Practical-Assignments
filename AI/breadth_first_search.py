from collections import deque 

class TreeNode:
    def __init__(self , val=0 , left=None , right=None):
        self.val=val
        self.right=right
        self.left=left

def bfs(root):
    if not root:
        return [] 
    
    result=[] 
    queue=deque() 
    queue.append(root) 

    while queue:
        level_size=len(queue) 
        level_values=[] 
        for _ in range(level_size):
            node=queue.popleft() 
            level_values.append(node.val) 

            if node.left:
                queue.append(node.left) 
            if node.right:
                queue.append(node.right) 
        result.append(level_values)  
    return result 

root=TreeNode(1) 
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(5) 
root.left.right=TreeNode(7)
root.right.left=TreeNode(6) 

bfs_result=bfs(root)  
print(bfs_result) 

#output-[[1], [2, 3], [5, 7, 6]]
 
