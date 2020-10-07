"""
Write a function to find the longest common prefix string
amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

import math


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs is None or len(strs) == 0:
            return ""

        shortest = math.inf

        for string in strs:
            shortest = min(shortest, len(string))

        index = 0
        while index < shortest:
            c = strs[0][index]
            for string in strs:
                if c != string[index]:
                    return string[:index]

            index += 1

        return strs[0][:index] if index > 0 else ""
