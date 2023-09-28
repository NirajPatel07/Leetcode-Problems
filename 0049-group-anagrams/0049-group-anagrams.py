class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        
        for word in strs:
            curr_word = list(word)
            curr_word.sort()
            curr_word = ''.join(curr_word)
            
            if curr_word in lookup:
                lookup[curr_word].append(word)
            else:
                lookup[curr_word] = [word]
                
        output = []
        for key, value in lookup.items():
            output.append(value)
        
        return output