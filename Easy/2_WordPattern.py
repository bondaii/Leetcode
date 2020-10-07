"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a
letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false

c_lookup {a -> dog}
w_lookup {dog -> a}
"""


def wordPattern(pattern: str, s: str) -> bool:
    words = s.split(" ")

    if len(words) != len(pattern):
        return False

    char_lookup = {}
    word_lookup = {}

    for i in range(len(pattern)):
        c = pattern[i]  # char from pattern
        w = words[i]  # word from splitted s i.e. words

        if c not in char_lookup:
            if w in word_lookup:
                return False

            char_lookup[c] = w
            word_lookup[w] = c
        else:
            if char_lookup[c] != w:
                return False
    return True


print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))
print(wordPattern("", ""))
