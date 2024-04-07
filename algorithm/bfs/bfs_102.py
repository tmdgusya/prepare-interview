# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque()
        answer = [[root.val]]
        queue.append((root, 0))

        while queue:
            acc = []
            for _ in range(len(queue)):
                root, idx = queue.pop()

                if root.left is not None:
                    acc.append(root.left.val)
                    queue.appendleft((root.left, idx + 1))
                
                if root.right is not None:
                    acc.append(root.right.val)
                    queue.appendleft((root.right, idx + 1))

                if root.left is None and root.right is None:
                    continue

                if len(acc) > 0:
                    if len(answer) - 1 < idx + 1:
                        # resize it
                        answer.append([])
                    answer[idx + 1] = acc

        return answer
        