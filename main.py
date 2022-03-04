# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# working solution, not efficient O(nlogn)
"""def recurbsearch(root, p):
    if not root: return False
    if not p: return True

    if root.val == p.val:
        return True
    else:
        if root.val > p.val:
            return recurbsearch(root.left, p)
        else:
            return recurbsearch(root.right, p)



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = [TreeNode()]
        count = [0]

        def lowestAncestor(root, p, q):
            if not recurbsearch(root, p) or not recurbsearch(root, q):
                return False
            if not lowestAncestor(root.left, p, q) and not lowestAncestor(root.right, p, q):
                if count[0] == 0:
                    node[0] = root
                    count[0] = 1
            return True

        lowestAncestor(root, p, q)
        return node[0]"""


# efficient solution, O(logn)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        current = root
        while current:
            if current.val > p.val and current.val > q.val:
                current = current.left
            elif current.val < p.val and current.val < q.val:
                current = current.right
            else:
                return current


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
