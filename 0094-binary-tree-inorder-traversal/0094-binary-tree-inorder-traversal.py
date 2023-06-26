# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#    1
#N/A   2
#    3

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        treeList = []
        self.inorderTraversalHelper(root, treeList)
        return treeList
        
    def inorderTraversalHelper(self, root: Optional[TreeNode], treeList: []):
        if root == None:
            return
        self.inorderTraversalHelper(root.left, treeList)
        treeList.append(root.val)
        self.inorderTraversalHelper(root.right, treeList)