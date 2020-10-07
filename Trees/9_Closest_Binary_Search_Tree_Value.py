"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closest = float('inf')

        def helper(root, value):
            if not root:
                return
            if abs(root.val - target) < abs(self.closest - target):
                self.closest = root.val

            # Target should be located on left subtree
            if target < root.val:
                helper(root.left, target)

            # target should be located on right subtree
            if target > root.val:
                helper(root.right, target)

        helper(root, target)
        return self.closest
