# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
#PREORDER TRAVERSAL
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        p_ans = []
        self.preorder(root, p_ans)
        return p_ans

    def preorder(self, root: TreeNode, p_ans : List[int]):
        if root:
            p_ans.append(root.val)
            self.preorder(root.left, p_ans)
            self.preorder(root.right, p_ans)

#POSTORDER TRAVERSAL
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        pos_ans = []
        self.pos(root, pos_ans)
        return p_ans

    def postorder(self, root: TreeNode, pos_ans : List[int]):
        if root:
            self.preorder(root.left, pos_ans)
            self.preorder(root.right, pos_ans)
            pos_ans.append(root.val)


#INORDER TRAVERSAL
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.inorder(root, ans)
        return ans

    def inorder(self, root: TreeNode, ans : List[int]):
        if root:
            self.inorder(root.left, ans)
            ans.append(root.val)
            self.inorder(root.right, ans)
