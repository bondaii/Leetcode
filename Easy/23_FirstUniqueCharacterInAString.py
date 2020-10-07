"""
Given a string, find the first non-repeating character in it
and return its index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
Note: You may assume the string contains only lowercase English letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = -1

        lookup = {}

        for i in range(len(s)):
            if s[i] in lookup:
                lookup[s[i]] = -1
            else:
                lookup[s[i]] = i

        for val in lookup.values():
            if val >= 0:
                result = min(result, val) if result >= 0 else val

        return result
