class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(left, right, stack, brackets):
            if left == right == 0:
                result.append(brackets)
                return
            
            if left > 0:
                backtrack(left-1, right, stack+1, brackets+"(")
            if right > 0 and stack > 0:
                backtrack(left, right-1, stack-1, brackets+")")
            
        backtrack(n, n, 0, "")
        
        return result