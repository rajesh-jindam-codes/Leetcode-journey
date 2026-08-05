class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for i in range(len(nums)):
            curr=nums[i]
            count=0
            while curr>0:
                count+=1
                curr/=10
            if count%2==0:
                total+=1
        return total