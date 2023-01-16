# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
    
        def dfs(node,seen):
            if not node:
                return 0
            if node.val in seen:
                seen.remove(node.val)
            else:
                seen.add(node.val)
            if not node.left and not node.right:
                return int(len(seen)<=1)

            return dfs(node.left,seen.copy()) + dfs(node.right,seen.copy())

        return dfs(root,set())
            