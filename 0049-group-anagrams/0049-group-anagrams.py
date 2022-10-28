class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        
        for word in strs:
            word_list = list(word)
            word_list.sort()
            
            curr_word = "".join(word_list)
            
            if curr_word in lookup:
                lookup[curr_word].append(word)
            else:
                lookup[curr_word] = [word]
                
        output = []
        for word_list in lookup:
            output.append(lookup[word_list])
            
        return output