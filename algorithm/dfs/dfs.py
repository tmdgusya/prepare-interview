import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional

def dfs(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    printed = [root.val]
    stack = deque()
    stack.appendleft(root)
    
    while stack:
        root = stack.popleft()
        printed.append(root.val)
        
        if root.left is not None:
            stack.appendleft(root.left)
        
        if root.right is not None:
            stack.appendleft(root.right)        
    
    return printed

class TestDfs(unittest.TestCase):
    
    def test_01(self):
        # create example tree for dfs using TreeNode
        #    1
        #   / \
        #  2   3
        #     / \
        #    4   5
        #   /
        #  6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.right.left.left = TreeNode(6)
        
        # should be same as [1,3,5,4,6,2]
        result = dfs(root=root)
        print(result)
        self.assertEqual(result, [1,3,5,4,6,2])