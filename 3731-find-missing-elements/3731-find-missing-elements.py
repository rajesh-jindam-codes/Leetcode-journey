class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans=[]
        for i in range(len(nums)-1):
            curr=nums[i]
            nxt=nums[i+1]
            while curr+1<nxt:
                ans.append(curr+1)
                curr+=1
        return ans