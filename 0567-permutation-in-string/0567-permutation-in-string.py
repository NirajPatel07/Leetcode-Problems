class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)                   # Example: s1 = "abi"  s2 = "eidbiaoo"
                                                    # ctr1 = {b:2, a:1, i:1}
        ctr1, ctr2 = Counter(s1), Counter(s2[:n1])  
                                                    #  i     ctr2                  ctr1 == ctr2 
        for i in range(n1,n2):                      # ––––   –––––––––––––––       ––––––––––––
            if ctr1 == ctr2: return True            #  4     {e:1, i:1, d:1, b:1}      False
                                                    #  5     {b:2, i:1, d:1}           False
            ctr2[s2[i-n1]]-= 1                      #  6     {b:2, a:1, i:1}           True
            ctr2[s2[i   ]]+= 1

        return ctr1 == ctr2