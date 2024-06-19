
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 如果根节点不存在，返回深度为0
        if not root:
            return 0
        # 如果根节点左右子树都不存在，返回深度为1
        if not root.left and not root.right:
            return 1
        # 如果根节点左子树不存在，返回右子树深度加1
        if not root.left:
            return self.minDepth(root.right) + 1
        # 如果根节点右子树不存在，返回左子树深度加1
        if not root.right:
            return self.minDepth(root.left) + 1
        # 如果根节点左右子树都存在，返回左右子树深度的较小值加1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
# leetcode submit region end(Prohibit modification and deletion)
