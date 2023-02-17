# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root is None:
            return
        
        self.minDiffInBST(root.left)

        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
		
        self.minDiffInBST(root.right)
        return self.res