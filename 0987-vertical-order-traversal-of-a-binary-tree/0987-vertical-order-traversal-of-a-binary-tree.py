# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        min_level, max_level = float("inf"), -float("inf")
        def dfs(node, level, order):
            if not node:
                return
            
            nonlocal min_level, max_level
            min_level = min(level, min_level)
            max_level = max(level, max_level)
            
            levels[level].append((order, node.val))
            
            dfs(node.left,  level-1, order+1)
            dfs(node.right, level+1, order+1)
        
        dfs(root, 0, 0)
        return [[j for i,j in sorted(levels[i])] for i in range(min_level,max_level+1)]
        