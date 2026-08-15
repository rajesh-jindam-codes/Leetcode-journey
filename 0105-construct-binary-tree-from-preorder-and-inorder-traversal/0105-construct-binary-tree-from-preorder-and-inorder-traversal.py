# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        indexMap={value:i for i,value in enumerate(inorder)}
        preorderIndex=[0]
        def helper(left,right):
            if left>right:
                return None
            rootVal=preorder[preorderIndex[0]]
            preorderIndex[0]+=1
            root=TreeNode(rootVal)

            mid=indexMap[rootVal]
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root
        return helper(0,len(inorder)-1)