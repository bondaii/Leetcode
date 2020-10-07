"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

"""

class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or len(s)==0:
            return True

        stack = []

        lookup = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for c in s:
            if c in lookup:
                stack.append(c)
                continue

            # c==')', '('
            if len(stack)==0:
                return False

            top = stack.pop()
            if lookup[top] != c:
                return False

        return len(stack)==0
