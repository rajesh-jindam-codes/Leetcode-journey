class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)
        return result