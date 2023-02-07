from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        # Fruit count in baskets
        basket = defaultdict(int)
        
        # Pointers to keep track of subarray
        l, r = 0, 0
        
        # Max number of fruits that can be picked
        max_fruits = 0
        
        # Iterate through fruit array
        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            
            # If there is more then 2 fruits
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
                
            max_fruits = max(max_fruits, r - l + 1)
            
        return max_fruits
