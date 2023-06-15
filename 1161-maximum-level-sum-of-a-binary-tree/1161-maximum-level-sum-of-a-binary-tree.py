# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        mapping = defaultdict(list)
        queue = deque([root])
        
        level = 1
        while(queue):
            _sum = 0
            _siz = len(queue)
            
            for _ in range(_siz):
                node = queue.popleft()
                _sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            mapping[_sum].append(level)
            level += 1

        return mapping[max(mapping.keys())][0]