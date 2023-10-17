class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        res = True

        def step(node):
            nonlocal res
            # сhecking for loops
            if node in set_:
                res = False
                return
            set_.add(node)

            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    step(child)
        
        # find a root (absent in children)
        set_ = set(range(n))
        set_.difference_update(leftChild, rightChild)
        if len(set_) != 1:
            return False
        
        step(set_.pop())

        return res and len(set_) == n