class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s=str(num)
        changes=False
        result=''
        for ch in s:
            if ch=='6' and not changes:
                result+='9'
                changes=True
            else:
                result+=ch
        return int(result)