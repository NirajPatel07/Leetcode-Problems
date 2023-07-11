class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        sorted_list = sorted(strs, key=len)
        print(sorted_list)
        
        for i, c in enumerate(sorted_list[0]):
            for s in sorted_list[1:]:
                if s[i] != c:
                    return sorted_list[0][:i]
        
        return sorted_list[0]
        