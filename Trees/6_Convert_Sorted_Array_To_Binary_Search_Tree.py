"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None or len(nums) == 0:
            return None

        return self.helper(nums, 0, len(nums))

    def helper(self, nums, lo, up):
        if lo == up:
            return

        mid = lo + (up-lo)//2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, lo, mid)
        node.right = self.helper(nums, mid+1, up)

        return node
