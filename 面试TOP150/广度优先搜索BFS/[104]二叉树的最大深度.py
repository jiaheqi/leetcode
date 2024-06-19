
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    递归遍历
    """
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 如果没有根节点，深度为0
        if not root:
            return 0
        # 如果根节点没有左子树和右子树，深度为1
        if not root.left and not root.right:
            return 1
        # 如果根节点没有左子树，则深度为右子树深度加1
        if not root.left:
            return self.maxDepth(root.right) + 1
        # 如果根节点没有右子树，则深度为左子树深度加1
        if not root.right:
            return self.maxDepth(root.left) + 1
        # 如果根节点左右子树都有，则深度为左右子树深度的较大值加1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    """
    迭代遍历
    """
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 如果没有根节点，深度为0
        if not root:
            return 0
        # 创建一个队列，将根节点加入队列
        queue = [root]
        # 创建一个变量，记录深度
        depth = 0
        # 循环遍历队列
        while queue:
            # 获取队列长度
            size = len(queue)
            # 循环遍历
            for i in range(size):
                # 弹出队列的第一个元素
                node = queue.pop(0)
                # 如果弹出的元素有左子树，则将左子树加入队列
                if node.left:
                    queue.append(node.left)
                # 如果弹出的元素有右子树，则将右子树加入
                if node.right:
                    queue.append(node.right)
            # 每queue循环一次，深度加1
            depth += 1
            return depth


        
# leetcode submit region end(Prohibit modification and deletion)
