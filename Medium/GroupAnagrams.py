'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}

        result = []
        for i, word in enumerate(strs):
            word_sorted = ''.join(sorted(word))

            if word_sorted in lookup:
                lookup[word_sorted].append(word)
            else:
                lookup[word_sorted] = [word]

        for words in lookup.values():
            result.append(words)

        return result
