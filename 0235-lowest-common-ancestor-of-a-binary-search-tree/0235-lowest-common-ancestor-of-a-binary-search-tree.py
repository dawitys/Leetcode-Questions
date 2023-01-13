# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findLCA(node, p,q):
            if p.val <= node.val <= q.val or p.val >= node.val >= q.val:
                return node
            elif p.val <= node.val and q.val <= node.val:
                return findLCA(node.left, p,q)
            else:
                return findLCA(node.right, p,q)
            
            
        return findLCA(root,p,q)