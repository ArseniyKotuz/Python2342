class Solution:
    def helper(self , root , List):
        if root == None : 
            return 
        self.helper(root.left , List)
        List.append(root.val)
        self.helper(root.right , List)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        List = []
        if root == None: return List
        self.helper(root , List)
        return List
