class Solution:
    def check(self, trie, word, widx):
        if widx == len(word): 
            return True
        
        t = trie
        ret = False
        
        for cidx in range(widx, len(word)):
            if word[cidx] in t:
                t = t[word[cidx]]
            else: 
                return False 
            
            if '#' in t: 
                ret |= self.check(trie, word, cidx+1)
                
            if ret: 
                return ret
                
        return ret
    
    def insert(self, word, trie):
        t = trie
        for c in word:
            if c not in t:
                t[c] = {}
                
            t = t[c]
        t['#'] = {}
            
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        t = {}
        ans = []
        for w in words:
            if self.check(t, w, 0):
                ans.append(w)
            self.insert(w, t)
            
        return ans