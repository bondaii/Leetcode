'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo = 0
        hi = 0

        if s is None or len(s) == 0:
            return 0

        result = -math.inf
        lookup = set()

        while hi < len(s):
            if s[hi] in lookup:
                lookup.remove(s[lo])
                lo += 1
            else:
                lookup.add(s[hi])
                result = max(result, len(lookup))
                hi += 1

        return result
