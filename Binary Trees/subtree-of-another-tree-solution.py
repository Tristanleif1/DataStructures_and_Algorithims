# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not subRoot:
            return True

        if self.isSame(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSame(self, r, t):

        if not r and not t:
            return True

        if not r or not t:
            return False

        while r and t and r.val == t.val:
            return self.isSame(r.left, t.left) and self.isSame(r.right, t.right)

        return False