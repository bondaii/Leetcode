"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        lookup = {}
        
        if len(s) != len(t):
            return False
        
        for _,c in enumerate(s):
            if c in lookup:
                lookup[c] += 1
            else:
                lookup[c] = 1
        
        for _,c in enumerate(t):
            if c in lookup:
                if lookup[c] <= 0:
                    return False
                else:
                    lookup[c] -= 1
            else:
                return False
        
        return True
        