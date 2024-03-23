# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''def get_values(self, p, values):
        if p is not None:
            values.append(p.val)
        self.get_values(p.left, values)
        self.get_values(p.right, values)
        return values

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        values = []
        if p is not None:
            p_root = p
            p_values = self.get_values(p_root, values)
        if q is not None:
            q_root = q
            q_values = self.get_values(q_root, values)
        if p==q:
            return True
        else:
            return False'''
    
    def check_value(p_value, q_value):
        if p_value == q_value:
            return True
        else:
            return False
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val!=q.val:
            return False
            
        lft = self.isSameTree(p.left,q.left)
        rht = self.isSameTree(p.right,q.right)
        # print(p_values, q_values)
        return lft and rht