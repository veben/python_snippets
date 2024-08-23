from typing import Optional


# Definition of a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive version
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        remaining = targetSum - root.val

        return self.hasPathSum(root.left, remaining) or self.hasPathSum(
            root.right, remaining
        )

    # Iterative version
    def hasPathSumIterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum)]

        while stack:
            node, current_sum = stack.pop()

            if not node.left and not node.right and current_sum == node.val:
                return True

            if node.right:
                stack.append((node.right, current_sum - node.val))
            if node.left:
                stack.append((node.left, current_sum - node.val))

        return False
