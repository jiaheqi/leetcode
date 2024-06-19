from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    递归实现
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def is_mirror(left, right):
            # 递归终止条件: 左右子树都为空, 或者左右子树其中一个为空，或者值不相等
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            # 递归调用 判断左子树和右子树是否对称：即左子树的左子树和右子树的右子树对称，左子树的右子树和右子树的左子树对称
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)

    """
    迭代实现：BFS
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            # 每次取出队列中前两个节点
            left = queue.pop(0)
            right = queue.pop(0)
            # 如果左右子树都为空，则继续循环
            if not left and not right:
                continue
            # 如果左右子树只有一个为空，则返回False
            if not left or not right:
                return False
            # 如果左右子树值不相等，则返回False
            if left.val != right.val:
                return False
            # 将左子树和右子树左右子树依次入队
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
            return True


if __name__ == '__main__':
    print(Solution().isSymmetric(
        TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))))

# leetcode submit region end(Prohibit modification and deletion)
