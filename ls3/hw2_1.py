class Solution():
    def inorderTraversal(self, root ):
        if root==None:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
