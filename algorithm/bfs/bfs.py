# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        It will be checking the whether those are same tree or not
        So, we shoulud check all the nodes in tree, and level.
        I'm gonna do BFS for both trees, and storing the values and queue
        and popping it, and comparing it
        """
        if (p != None and q == None) or (p == None and q != None):
            return False
        left_queue = deque()
        left_queue.append(p.val)
        right_queue = deque()
        right_queue.append(q.val)

        left_print = []
        right_print = []

        while left_queue:
            for _ in range(len(left_queue)):
                root = left_queue.popleft()
                
                if root.left is not None:
                    left_queue.append(root.left)
                    left_print.append(root.left.val)

                if root.right is not None:
                    left_queue.append(root.right)
                    left_print.append(root.right.val)
        while right_queue:
            for _ in range(len(left_queue)):
                root = right_queue.popleft()
                
                if root.left is not None:
                    right_queue.append(root.left)
                    right_print.append(root.left.val)

                if root.right is not None:
                    right_queue.append(root.right)
                    right_print.append(root.right.val)

        if len(left_print) != len(right_prin):
            return False

        for i in range(len(left_print)):
            if left_print[i] != right_print[i]:
                return False
        
        return True
