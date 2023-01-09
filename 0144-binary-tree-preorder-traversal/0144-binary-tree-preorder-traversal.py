class Solution:
    def preorderTraversal(self, root_: TreeNode | None) -> list[int]:
        # Morris (Destroys the tree)
        def preorder(root: TreeNode | None) -> Iterable:
            node = root
            while node:
                if node.left is None:
                    yield node.val
                    node = node.right
                    continue

                last = node.left
                while last.right:
                    last = last.right
                last.right = node.right

                yield node.val
                node = node.left
                
        return list(preorder(root_))