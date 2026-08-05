class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left=0
        right=len(nums)-1
        maxi=0
        while left<right:
            maxi=max(maxi,nums[left]+nums[right])
            left+=1
            right-=1
        return maxi