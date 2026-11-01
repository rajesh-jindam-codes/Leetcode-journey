# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        prev=None
        count=0
        maxCount=0
        result=[]
        def inorder(node):
            nonlocal prev,count,maxCount,result

            if not node:
                return
            inorder(node.left)
            if prev==node.val:
                count+=1
            else:
                count=1
            if count>maxCount:
                maxCount=count
                result=[node.val]
            elif count==maxCount:
                result.append(node.val)
            prev=node.val
            inorder(node.right)
        inorder(root)
        return result