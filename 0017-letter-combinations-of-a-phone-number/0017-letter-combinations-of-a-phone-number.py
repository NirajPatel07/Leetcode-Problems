class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        mapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        result = [""]
        
        for digit in digits:
            tmp = []
            
            for c in mapping[digit]:
                for r in result:
                    tmp.append(r+c)
            
            result = tmp
            
        return result
            