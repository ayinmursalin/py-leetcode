class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longest = ""
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                word = s[i : j + 1]
                if self.isPalindrome(word) and len(word) > len(longest):
                    longest = word

        return longest  
            

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
