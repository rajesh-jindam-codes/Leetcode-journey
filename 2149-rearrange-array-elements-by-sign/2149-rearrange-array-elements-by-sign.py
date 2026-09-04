class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=[]
        neg=[]
        for num in nums:
            if num>=0:
                pos.append(num)
            else:
                neg.append(num)
        i=j=0
        result=[]
        while i<len(pos) and j<len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i+=1
            j+=1
        while i<len(pos):
            result.append(pos[i])
            i+=1
        while j<len(neg):
            result.append(neg[j])
            j+=1
        return result