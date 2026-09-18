class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        freq={}
        for num in arr1:
            freq[num]=freq.get(num,0)+1
        remaining=[]
        result=[]
        for num in arr2:
            if num in freq:
                for _ in range(freq[num]):
                    result.append(num)
                del freq[num]
        for num in freq:
            for _ in range(freq[num]):
                remaining.append(num)
        remaining.sort()
        result.extend(remaining)
        return result
