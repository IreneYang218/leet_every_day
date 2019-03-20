def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        now = [root]
        dep = 0
        while len(now)>0:
            dep += 1
            next = []
            for i in now:
                if i is not None:
                    if i.left is not None:
                        next.append(i.left)
                    if i.right is not None:
                        next.append(i.right)
            now = next
        return dep