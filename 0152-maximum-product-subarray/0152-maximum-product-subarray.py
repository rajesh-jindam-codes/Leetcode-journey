class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax=nums[0]
        currMin=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            if num<0:
                currMax,currMin=currMin,currMax
            currMax=max(num,currMax*num)
            currMin=min(num,currMin*num)
            ans=max(ans,currMax)
        return ans