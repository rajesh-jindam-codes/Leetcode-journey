class Solution(object):
    # class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n=len(text1)
        m=len(text2)
        prev=[-1 for _ in range(m+1)]
        for ind2 in range(m+1):
            prev[ind2]=0
        # for ind1 in range(n+1):
        #     dp[ind1][0]=0
        for ind1 in range(1,n+1):
            curr=[-1 for _ in range(m+1)]
            curr[0]=0
            for ind2 in range(1,m+1):
                if text1[ind1-1]==text2[ind2-1]:
                    curr[ind2]=1+prev[ind2-1]
                else:
                    curr[ind2]=max(prev[ind2],curr[ind2-1])
            prev=curr
        return prev[m]
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=s
        s2=s1[::-1]
        return self.longestCommonSubsequence(s1,s2)