"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

# recursive
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.helper(root.left, root.right)

    def helper(self, l, r):
        if not l and not r:
            return True

        if not l or not r:
            return False

        if l.val != r.val:
            return False

        return self.helper(l.left, r.right) and self.helper(l.right, r.left)

# iterative
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()

            if left is None and right is None:
                continue

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True
