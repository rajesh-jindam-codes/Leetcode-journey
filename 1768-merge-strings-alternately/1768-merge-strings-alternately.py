class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=[]
        i=j=0
        n=len(word1)
        m=len(word2)
        while i<n and j<m:
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1
        if i<n:
            while i<n:
                result.append(word1[i])
                i+=1
        if j<m:
            while j<m:
                result.append(word2[j])
                j+=1
        return "".join(result)