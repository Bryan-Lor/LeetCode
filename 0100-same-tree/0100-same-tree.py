# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1       1
#2      null 2

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        firstTree, secondTree = [], []
        self.bfs(p, firstTree)
        self.bfs(q, secondTree)
        
        print(firstTree, secondTree)
        if firstTree == secondTree: 
            return True
        else:
            return False
        
    def bfs(self, root: Optional[TreeNode], queue: []): #1 -> [1 2]
        if root is None:
            return queue.append(None)
            
        queue.append(root.val)
        self.bfs(root.left, queue)
        self.bfs(root.right, queue)
