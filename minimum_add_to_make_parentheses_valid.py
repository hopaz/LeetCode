class Solution:
   def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        left, right = 0, 0
        for s in S:
            if s=="(":
                left+=1
            else: # CLOSE case
                if left==0:
                    # This is unpaired
                    right+=1
                else:
                    left-=1
        return left+right


s = Solution()
str="((())"
print(s.minAddToMakeValid(str))
