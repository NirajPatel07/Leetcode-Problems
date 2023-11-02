class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        hashmap={}
        def rec(node):
            if node==None:
                return (0,0)
            n1,s1=rec(node.left)
            n2,s2=rec(node.right)
            n3=1+n1+n2
            s3=s1+s2+node.val
            hashmap[node]=(n3,s3)
            return (n3,s3)
        rec(root)
        c=0
        for i in hashmap:
            cur=hashmap[i]
            if i.val==cur[1]//cur[0]:
                c+=1
        return c