class Solution:
    def longestCommonSubsequence(self,text1,text2):
        n=len(text1)
        m=len(text2)
        dp=[[-1 for _ in range(m+1)]for _ in range(n+1)]
        for ind2 in range(m+1):
            dp[0][ind2]=0
        for ind1 in range(n+1):
            dp[ind1][0]=0
        for ind1 in range(1,n+1):
            for ind2 in range(1,m+1):
                if text1[ind1-1]==text2[ind2-1]:
                    dp[ind1][ind2]=dp[ind1-1][ind2-1]+1
                else:
                    dp[ind1][ind2]=max(dp[ind1-1][ind2],dp[ind1][ind2-1])
        return dp[n][m]
    def minInsertions(self,s):
        s1=s
        s2=s1[::-1]
        return len(s)-self.longestCommonSubsequence(s1,s2)
# obj=Solution()
# print(obj.minInsertions('zzazz'))