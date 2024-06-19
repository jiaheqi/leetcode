
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        迭代
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            size = len(queue)
            # 存储每一层的节点
            level = []
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

    def levelOrder(self, root):
        """
        递归
        """
        if not root:
            return []
        res = []
        # depth 为当前节点所在的层数
        def dfs(node, depth):
            if not node:
                return
            # 如果当前层数等于res的长度，说明当前层还没有添加节点，则添加一个空列表占位
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            # 递归遍历左右子树
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        # 从根节点开始遍历
        dfs(root, 0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
