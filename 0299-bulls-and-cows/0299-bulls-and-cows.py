class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Dictionary for Lookup
        lookup = Counter(secret)
        
        x, y = 0, 0
        
        """ The reason for using two for loop is in this problem we have to give             first priority to number which are at correct position, Therefore we are             first updating x value """
        
        # First finding numbers which are at correct position and updating x
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                x+=1
                lookup[secret[i]]-=1
        
        # Finding numbers which are present in secret but not at correct position 
        for i in range(len(guess)):
            if guess[i] in lookup and secret[i] != guess[i] and lookup[guess[i]]>0:
                y+=1
                lookup[guess[i]]-=1
        
        return "{}A{}B".format(x, y)