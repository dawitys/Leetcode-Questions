# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = defaultdict(list)
        
        @lru_cache(None)
        def preorder(root):
            if root==None:
                return tuple([-float('inf')])
            return tuple([root.val] + list(preorder(root.left)) + list(preorder(root.right)))

        def dfs(node):
            if not node:
                return
            pre = preorder(node)
            res[pre].append(node)
                
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return [res[r][0] for r in res if len(res[r])>1]