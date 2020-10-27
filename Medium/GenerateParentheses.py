'''
Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''


class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(output_list, parens, opens, closes, size):
            if len(parens) == 2*size:
                output_list.append(parens)
                return

            if opens < size:
                backtrack(output_list, parens+'(', opens+1, closes, size)
            if closes < opens:
                backtrack(output_list, parens+')', opens, closes+1, size)

        backtrack(result, '', 0, 0, n)

        return result
