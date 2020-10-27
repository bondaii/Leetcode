'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [0]*(len(s)+1)

        if s is None or len(s) == 0:
            return 0

        cache[0] = 1
        cache[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(s)+1):
            single = int(s[i-1: i])
            double = int(s[i-2: i])

            if 0 < single < 10:
                cache[i] = cache[i-1]
            if 10 <= double <= 26:
                cache[i] += cache[i-2]

        return cache[len(s)]
