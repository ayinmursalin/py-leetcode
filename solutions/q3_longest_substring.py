class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        
        max_value = 0
        
        for i in range(0, length):
            chars = ""
            for j in range(i, length):
                if s[j] in chars:
                    max_value = max(len(chars), max_value)
                    break
                
                chars += s[j] 
                    
            max_value = max(len(chars), max_value)
        
        return max_value
        