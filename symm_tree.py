
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        self.list_left = []
        self.list_right = []
        self.walk_tree_left(root)
        self.walk_tree_right(root)
        if self.list_left == self.list_right:
            return True
        else: return False
        
    def walk_tree_left(self, root):
        if root is None: return self.list_left.append(None)
        self.list_left.append(root.val)
        self.walk_tree_left(root.left)
        self.walk_tree_left(root.right)
    
    def walk_tree_right(self, root):
        if root is None: return self.list_right.append(None)
        self.list_right.append(root.val)
        self.walk_tree_right(root.right)
        self.walk_tree_right(root.left)

# Better version

    def isSymmetric_iter(self, root):
        now = []
        if root:
            now.append(root)
        while now:
            vals = []
            for i in now:
                if i:
                    vals.append(i.val)
                else:
                    vals.append(None)
            if list(reversed(vals)) != vals:
                return False
            else:
                now = [j for i in now if i for j in (i.left, i.right)]
        return True

    def isSymmetric_recur(self, root):
        def sym_tree(L,R):
            if L and R: 
                return L.val == R.val and sym_tree(L.left, R.right) and sym_tree(L.right, R.left)
            else:
                return L == R
        return sym_tree(root, root)

