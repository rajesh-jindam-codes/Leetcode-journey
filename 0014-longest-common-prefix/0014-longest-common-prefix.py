class Solution(object):
    def longestCommonPrefix(self, strs):
        result=""
        base=strs[0]
        for i in range(0,len(base)):
            for word in strs[1:]:
                if i==len(word) or word[i]!=base[i]:
                    return result
            result+=base[i]
        return result