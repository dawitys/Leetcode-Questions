# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        q = deque([root])
        
        while(q):
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr)
            for l in level:
                if l.left:
                    q.append(l.left)
                if l.right:
                    q.append(l.right)
            ans.append([l.val for l in level])
        
        
        return ans