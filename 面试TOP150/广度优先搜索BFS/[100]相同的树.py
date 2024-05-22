# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 如果同时为None，相等
        if p is None and q is None:
            return True
        # 如果只有其中一个为None，不相等
        if p is None or q is None:
            return False
        # 将p，q初始化为队列先进先出
        search_queue_p = deque([p])
        search_queue_q = deque([q])
        # 只要有一个队列pop为空，结束循环
        while search_queue_p and search_queue_q:
            search_p = search_queue_p.popleft()
            search_q = search_queue_q.popleft()
            print(search_p)
            print(search_p.left)
            if search_p and search_q:
                # 如果根节点就不相等，直接返回False
                if search_p.val != search_q.val:
                    return False
                # 如果左右子树都存在，则将左右子树分别加入队列，这样队列中就存在p.left,p.right,q.left,q.right，分别IE比较对应的val
                # 不能直接比较左右子树的val，因为队列中只存在节点p，并不存在p.left,p.right
                if search_p.left and search_q.left:
                    search_queue_p.append(search_p.left)
                    search_queue_q.append(search_q.left)
                if search_p.right and search_q.right:
                    search_queue_p.append(search_p.right)
                    search_queue_q.append(search_q.right)
                # 判断左右子树是否同时存在，同时不存在，其中一个存在另一个不存在的时候返回False
                if search_p.left and not search_q.left:
                    return False
                if search_p.right and not search_q.right:
                    return False
                if not search_p.left and search_q.left:
                    return False
                if not search_p.right and search_q.right:
                    return False
            else:
                return False
        # 循环结束时判断是否两个队列同时为空，同时为空说明比较了每个节点，且都没有返回False，则说明相等
        result = not search_queue_q and not search_queue_q
        return result


if __name__ == '__main__':
    # 初始化两个二叉树用于测试
    # 树1
    p = TreeNode(1)
    # p.left = TreeNode(2)
    # p.right = TreeNode(3)
    # 树2
    q = TreeNode(1)
    q.left = TreeNode(None)
    q.right = TreeNode(3)

    # 创建 Solution 实例并进行测试
    solution = Solution()
    result = solution.isSameTree(p, q)
    print("两棵树是否相同:", result)
