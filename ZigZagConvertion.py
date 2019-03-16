class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows >= len(s):
            return s
        
        row_string = ['']*numRows
        
        s_ptr = 0
        r_ptr = 0
        increasing = False
        
        
        while s_ptr < len(s):          
            row_string[r_ptr] += s[s_ptr]
            
            if r_ptr == numRows-1 or r_ptr == 0:
                increasing = not increasing
            
            if increasing:
                r_ptr += 1
            else:
                r_ptr -= 1
            s_ptr += 1
        
        return ''.join(row_string)

s = Solution()
string1 = "PAYPALISHIRING"
results = s.convert(string1, 4)
print(results)
print("test")
