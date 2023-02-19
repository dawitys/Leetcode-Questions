# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        q.append(root)
        
        if not root: return []
        
        reverse = False
        while(q):
            level = []
            for i in range(len(q)):
                level.append(q.popleft())

            if reverse:
                ans.append([n.val for n in reversed(level)])
            else:
                ans.append([n.val for n in level])
                
            reverse = not reverse
            
            for node in level:
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                    
        return ans
                
        