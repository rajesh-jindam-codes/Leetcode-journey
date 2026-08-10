# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=deque([root])
        lefttoRight=True
        result=[]
        while queue:
            level=[]
            levelSize=len(queue)
            for i in range(levelSize):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not lefttoRight:
                level.reverse()
            result.append(level)
            lefttoRight=not lefttoRight
        return result