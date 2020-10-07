"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert s to lower
        # only alphanumeric
        if s is None or len(s)==0:
            return True
        
        s = s.strip()
        s = s.lower()
        
        lo = 0
        hi = len(s)-1
        
        while lo <= hi :
            if not s[lo].isalnum():
                lo += 1
                continue
            if not s[hi].isalnum():
                hi -= 1
                continue
            
            if s[lo] != s[hi]:
                return False
            
            lo += 1
            hi -= 1
        
        return True