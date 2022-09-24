from typing import  Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #检查是否是树
        if not root:
            return False
        #检查是否到达叶子节点
        if not root.left and not root.right:
            return  sum == root.val
        #简化问题:将 是否存在 从节点root到叶子节点的路径,满足路径和=sum
        #转化为:从当前节点的子节点,到叶子的路径,满足其路径和为 sum - val
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)